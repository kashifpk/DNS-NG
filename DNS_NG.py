import sys
from twisted.internet import reactor
from twisted.names import dns
from twisted.names import client, server
from twisted.names.server import DNSServerFactory
from sqlalchemy.orm.exc import NoResultFound

import db_code
from db_model import DNSRequest, ClientHost, Redirect
from redirect_manager import RedirectManager


class MyDNSServerFactory(DNSServerFactory):
    dnsDB = None
    RM = None # RedirectManager
    
    def __init__(self, authorities=None, caches=None, clients=None, verbose=0):
        self.RM = RedirectManager()
        DNSServerFactory.__init__(self, authorities=authorities, caches=caches, clients=clients, verbose=verbose)
    
    
    def sendReply(self, protocol, message, address):
        
        s = ' '.join([str(a.payload) for a in message.answers])
        auth = ' '.join([str(a.payload) for a in message.authority])
        add = ' '.join([str(a.payload) for a in message.additional])
        
        host = str(address[0])
        queries = []
        output = "Query from: %s for:\n" % host
        
        
        for q in message.queries:
            queries.append({'domain': q.name.name, 'type': dns.QUERY_TYPES[q.type], 
                            'class': dns.QUERY_CLASSES[q.cls]})
            output += "    %s [%s] [%s]" % (q.name.name, dns.QUERY_TYPES[q.type], dns.QUERY_CLASSES[q.cls])
        
        print(output)
        #print(s)
        #print(auth)
        #print(add)
        
        if self.dnsDB is not None:
            #record the query into the DB
            obj_host = None
            
            #check if the host is already present
            try:
                obj_host = self.dnsDB.query(ClientHost).filter_by(host_ip=host).one()
            except NoResultFound, e:
                obj_host = ClientHost(host)
                self.dnsDB.add(obj_host)
                obj_host = self.dnsDB.query(ClientHost).filter_by(host_ip=host).one()
                
            
            
            for query in queries:
                req = DNSRequest(obj_host.host_id, query['domain'], query['type'])
                self.dnsDB.add(req)
        
        
        if address is None:
            protocol.writeMessage(message)
        else:
            #print host, message.queries[0].name.name, dns.QUERY_TYPES[message.queries[0].type]
            redirect_ip = self.RM.get_redirect_ip(host, message.queries[0].name.name, dns.QUERY_TYPES[message.queries[0].type])
            #print redirect_ip
            
            if redirect_ip:
                print("Applying redirection .... ")
                
                #create a dummy record for testing
                rec = dns.Record_A(redirect_ip, 5)
                #print(rec)
                for a in message.answers:
                    #print repr(a)
                    if a.type == message.queries[0].type:
                        a.payload = rec
                
                #print(message.answers)
            
            protocol.writeMessage(message, address)
        
        
        


if '__main__' == __name__:
    
    if 'setup_db' in sys.argv:
        db_code.setup_db()
        print "Database tables created!"
    
    db_session = db_code.get_db_session()
    #resolver = client.Resolver(servers=[('192.168.1.254', 53)])
    resolver = client.Resolver('/etc/resolv.conf')   #just use system settings for resolving queries
    
    factory = MyDNSServerFactory(clients=[resolver])
    factory.dnsDB = db_session
    
    protocol = dns.DNSDatagramProtocol(factory)

    reactor.listenUDP(53, protocol)
    reactor.listenTCP(53, factory)
    reactor.run()



    
    
    

    
