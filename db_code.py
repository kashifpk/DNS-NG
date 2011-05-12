from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from config import db_type, db_host, db_name, db_pass, db_user
import db_model

def setup_db():
    "Creates database tables. Called if the database is not setup"
    
    engine = create_engine("%s://%s:%s@%s/%s" % (db_type, db_user, db_pass, db_host, db_name), echo=True)
    db_model.Base.metadata.bind = engine
    db_model.Base.metadata.create_all()

def get_db_session():
    "Returns database session object"
    engine = create_engine("%s://%s:%s@%s/%s" % (db_type, db_user, db_pass, db_host, db_name))
    Session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine))
    
    return Session()
