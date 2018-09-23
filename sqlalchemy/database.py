# _*_ coding: utf-8 _*_
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# echo = True,will show generated sql.
# The echo flag is a shortcut to setting up SQLAlchemy logging, which is accomplished via Python’s standard logging module
#the SQLite dialect will interpret instructions to the Python built-in sqlite3 module.
# lazy Connecting, will connect to db will first time it is asked to perform a task

#db engine (sqlite)
database_file = os.path.join(os.path.abspath(os.path.dirname(__file__)),'samples.db')
#engine = create_engine('sqlite:///:memory:' echo=True)
engine = create_engine('sqlite:///' + database_file, echo=True, convert_unicode=True)

#create base class
#Declarative, which allows us to create classes that include directives to describe the actual database table they will be mapped to.
Base = declarative_base()


#session 
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
#query
Base.query = db_session.query_property()


def init_db():
    #because create a __init__.py in model forlder, we can import it!
    from model.user import User
    Base.metadata.create_all(bind=engine)