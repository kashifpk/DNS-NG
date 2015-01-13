import sys
from twisted.internet import reactor
from twisted.names import dns
from twisted.names import client, server
from twisted.names.server import DNSServerFactory
from sqlalchemy.orm.exc import NoResultFound

import db_code
from db_model import DNSRequest, ClientHost, Redirect
from redirect_manager import RedirectManager

reload_redirects = False
no_logging = False

from .dns_factory import DNSNGServerFactory


if '__main__' == __name__:
    import os
    
    import procname
    procname.setprocname('DNS_NG')
    
    if '--setup_db' in sys.argv:
        db_code.setup_db()
        print("Database tables created!")
    
    if '--daemon' in sys.argv:
        from createDaemon import createDaemon
        retCode = createDaemon()
        
    if '--reload_redirects' in sys.argv:
        reload_redirects = True
    
    if '--no-logging' in sys.argv:
        no_logging = True
    
    db_session = db_code.get_db_session()
    #resolver = client.Resolver(servers=[('192.168.1.254', 53)])
    resolver = client.Resolver('/etc/resolv.conf')   #just use system settings for resolving queries
    
    factory = MyDNSServerFactory(clients=[resolver])
    factory.dnsDB = db_session
    
    protocol = dns.DNSDatagramProtocol(factory)

    reactor.listenUDP(53, protocol)
    reactor.listenTCP(53, factory)
    reactor.run()
