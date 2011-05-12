#!/usr/bin/env python

"""db.py
database interfacing class.
This component interfaces with the backend DB.
This acts as a DB tier (n-tiered approach) and helps isolate the DB functions so later
if the DB is to be switched to some other product (currently its MySQL) it can be done
easily by only modifying thise component.

Updates in version 0.2 (31-July-2006):
   - db_execute() method returns dictionaries for select statements now allowing by-key access
     to records instead of by-index access. This only works if the * wildcard is not used in select
     statement's field list.
     
Updates in version 0.2.1 (28-September-2006):
   - Fix bug in db_execute() method that returns field names as "distinct fieldname" for
     queries of the type "select distinct fieldname from table"

Updates in version 0.2.2 (12-July-2010 [Yes, it has been a while ;-)])
   - Support for debug mode. If set to True, all database statements are printed before execution.

Updates in version 0.2.3 (26-July-2010)
   - Now group function that take multiple parameters can be used in select statements. Previously fields were
     being split on ',' so field names like substr(myfield, 2, 5) confused the field_parsing code and query gave
     errors. Now there is a separate function _split_fields to process this correctly.
"""
__author__ = "Kashif Iftikhar"
__version__ = "0.2.3"

import MySQLdb
import sys

DB_HOST = 'localhost'
DB_NAME = 'mypydns'
DB_USER = 'mypydns'
DB_PASS = 'mypydns'

class db:
   'The DB class object interfaces with the mysql DBs for the crawler'
        
   def __init__ (self, host='localhost', db_name='mypydns', user='mypydns', passwd='mypydns'):
      'The constructor loads the apporopriate DB'
      self.db_name = db_name
      self.db_host = host
      self.db_user = user
      self.db_password = passwd
      self.debug = False

   def open_db(self):
      "Opens a connection to the database"
      self.connection = MySQLdb.connect(db=self.db_name, user=self.db_user, passwd=self.db_password, host=self.db_host)
      self.execute('set autocommit=1')
      
   def close_db(self):
      "Closes a connection to the database"
      self.connection = None
   
   def _split_fields(self, fields_str):
      fields = []
      
      sp_ch_count = {'"': 0, '(': 0, ')': 0}
      
      last_idx = 0
      idx = 0
      for c in fields_str:
         idx +=1
         if c in sp_ch_count.keys():
            if '"'==c:
               if 0==sp_ch_count['"']:
                  sp_ch_count['"']=1
               else:
                  sp_ch_count['"']=0
            
            elif '('==c:
               sp_ch_count['(']+=1
            elif ')'==c:
               sp_ch_count['(']-=1
            
         elif ','==c:
            if 0 == sp_ch_count['"'] and 0 == sp_ch_count['(']:
               fields.append(fields_str[last_idx:idx-1].strip())
               last_idx = idx
      
      fields.append(fields_str[last_idx:].strip())
      
      return fields
   
   def execute(self, query):
      "Executes the given query against the DB"
      try:
         query_type = ''
         if self.debug:
            print(query)
         
         c = self.connection.cursor()
         c.execute(query)
         results = c.fetchall()
         
         #check if the query is a select query, if yes, try returning a dictionary instead of a tuple.
         query_parts = query.split()
         if 'INSERT' == query_parts[0].upper():
            return self.connection.insert_id()
         elif 'SELECT' == query_parts[0].upper():
            uquery = query.upper()
            idx = uquery.find(' FROM ')
            field_list = query[6:idx].strip()
            
            if '*' != field_list.strip():
               fields = self._split_fields(field_list)
               #fields = field_list.split(',')
               #print repr(fields)
               fieldnames = []
               for field in fields:
                  #check if field contains a . (e.g, m.name etc.) and remove the dot and everything before the dot
                  dot_idx = field.find('.')
                  if -1 != dot_idx:
                     field = field[dot_idx+1:]
                     
                  idx = field.upper().find(' AS ')
                  
                  if -1 != idx:
                     fieldnames.append(field[idx+4:].strip())
                     
                  else:
                     #fixing the DISTRINCT keyword bug
                     field = field.strip()
                     idx = field.find(' ')
                     word = field[:idx].strip()
                     if 'DISTINCT' == word.upper():
                        field = field[idx+1:]
                     fieldnames.append(field)
               
               query_type = 'SELECT'
               new_results=[]
               for record in results:
                  d = {}
                  i=0
                  for fieldname in fieldnames:
                     d[fieldname] = record[i]
                     i += 1
                     
                  new_results.append(d)
                  
                  
         c.close()
      except (Exception), diag:
         ret = str(diag)
      else:
         if 'SELECT' == query_type:
            ret = new_results
         else:
            ret = results
      
      
      return ret



if __name__ == '__main__':
    import sys
    import string
    #print sys.argv[1]

    
    obj_db = db()
    obj_db.open_db()
    results = obj_db.execute('show tables')
    #results = obj_db.execute("select distinct station_id, station_name from stations")
    obj_db.close_db()
    #print type(results)
    print "Total Records: %d" % (len(results))
    print results
        
    


