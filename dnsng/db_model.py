from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship, backref


Base = declarative_base()

class ClientHost(Base):
    __tablename__ = 'client_hosts'
    
    host_id = Column(Integer, primary_key=True)
    host_ip = Column(String(20), unique=True)
    host_name = Column(String(250))
    
    def __init__(self, host_ip, host_name=''):
        self.host_ip = host_ip
        self.host_name = host_name
    
    def __repr__(self):
        return "<ClientHost('%s','%s')>" % (self.host_ip, self.host_name)


class DNSRequest(Base):
    __tablename__ = 'dns_requests'
    
    req_id = Column(Integer, primary_key=True)
    request_query = Column(String(250))
    query_type = Column(String(50))
    request_time = Column(DateTime, default=func.now())
    
    host_id = Column(Integer, ForeignKey('client_hosts.host_id'))
    
    host = relationship(ClientHost, backref=backref('dns_requests', order_by=host_id))
    
    def __init__(self, host_id, query, type):
        self.host_id = host_id
        self.request_query = query
        self.query_type = type
    
    def __repr__(self):
        return "<DNSRequest('%s','%s','%s')>" % (self.host.host_name, self.request_query, self.query_type)

class Redirect(Base):
    __tablename__ = 'redirects'
    
    rule_id = Column(Integer, primary_key=True)
    redirect_ip = Column(String(250))
    client_host_specs = Column(String(250))
    query_domain = Column(String(250))
    query_type = Column(String(50)) # A, AAAA, MX, SOA etc 
    enabled = Column(Boolean, default=True)
    
    def __init__(self, redirect_ip, client_host_specs, query_domain, query_type, enabled=True):
        self.redirect_ip = redirect_ip
        self.client_host_specs = client_host_specs
        self.query_domain = query_domain
        self.query_type = query_type
        self.enabled=enabled
    
    def __repr__(self):
        return "<Redirect('%s','%s','%s','%s',%s)>" % (self.redirect_ip, self.client_host_specs, self.query_domain, \
                                                       self.query_type, self.enabled)
    

    