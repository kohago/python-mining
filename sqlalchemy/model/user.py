from sqlalchemy import create_engine,Column,Integer,String
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    # __str__ __repr__ is the same
    # will be called when print(user)
    def __repr__(self):
        return "<user(name = '%s',fullname='%s',password='%s')>" % (name,fullname,password)

    def __init__(self,name=None,fullname=None,password=None):
        self.name = name
        self.fullname = fullname
        self.password = password