from db_model import Redirect, ClientHost, DNSRequest
from db_code import get_db_session
from pprint import pprint, pformat
import re

class RedirectManager():
    "class for loading and managing redirects"
    
    objDB = None
    redirects_table = []
    
    def __init__(self):
        "Create a RedirectManager object"
        
        self.objDB = get_db_session()
        self.load_redirects()
    
    def __repr__(self):
        return pformat(self.redirects_table )
    
    def load_redirects(self):
        "Load all redirects from database"
        #self.objDB.flush()
        #self.objDB.commit()
        redirects = self.objDB.query(Redirect)
        self.redirects_table = []
        for R in redirects:
            self.redirects_table.append({'redirect_ip': R.redirect_ip, 'query_type': R.query_type,
                                         'client_host_specs': R.client_host_specs, 'enabled': R.enabled,
                                         'query_domain': R.query_domain,
                                         'client_re': re.compile(R.client_host_specs),
                                         'domain_re': re.compile(R.query_domain)
                                         })
    
    
    def get_redirect_ip(self, client, query_domain, query_type):
        "Given a requesting client and a the requested domain, returns either None or the redirect IP for the domain (if present)"
        self.load_redirects()
        for R in self.redirects_table:
            
            if R['client_re'].match(client) and R['domain_re'].match(query_domain) and \
               query_type==R['query_type'] and R['enabled']:
                print("enabled: %s" % str(R['enabled']))
                return R['redirect_ip']
        
        return None
    