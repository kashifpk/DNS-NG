from twisted.internet import reactor
from twisted.names import dns
from twisted.names import client, server
from twisted.names.server import DNSServerFactory
from datetime import datetime
import db

def datetime_to_mysql_date(D):
    "Converts a datetime object to mysql datetime string"
    mysql_datetime = "%i-%i-%i %i:%i:%i" % (D.year, D.month, D.day, D.hour, D.minute, D.second)
    return(mysql_datetime)

class MyDNSServerFactory(DNSServerFactory):
    dnsDB = None
    
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
            host_id=0
            
            #check if the host is already present
            q = "select host_id from client_hosts where host_ip='%s'" % host
            res = self.dnsDB.execute(q)
            if len(res)>0:
                host_id= res[0]['host_id']
            else:
                q = "insert into client_hosts(host_ip) values('%s')" % host
                host_id = self.dnsDB.execute(q)
            
            request_time = datetime.now()
            for query in queries:
                q = "insert into dns_requests(host_id, request_query, query_type, request_time) " + \
                    "values(%i, '%s', '%s', '%s')" % (host_id, query['domain'], query['type'], datetime_to_mysql_date(request_time))
                
                self.dnsDB.execute(q)
        
        
        if address is None:
            protocol.writeMessage(message)
        else:
            if 'yahoo.com' == message.queries[0].name.name and 'A' == dns.QUERY_TYPES[message.queries[0].type]:
                print("Applying redirection .... ")
                #create a dummy record for testing
                rec = dns.Record_A('192.168.1.2', 300)
                for a in message.answers:
                    a.payload = rec
                
                #protocol.writeMessage('192.168.1.2', address)
                
                protocol.writeMessage(message, address)
            else:
                protocol.writeMessage(message, address)
        
        
        

if '__main__' == __name__:
    D = db.db()
    D.open_db()
    
    #resolver = client.Resolver(servers=[('192.168.1.254', 53)])
    resolver = client.Resolver('/etc/resolv.conf')   #just use system settings for resolving queries
    
    factory = MyDNSServerFactory(clients=[resolver])
    factory.dnsDB = D
    
    protocol = dns.DNSDatagramProtocol(factory)

    reactor.listenUDP(53, protocol)
    reactor.listenTCP(53, factory)
    reactor.run()

