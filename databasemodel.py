from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Float

Base=declarative_base()

class product(Base):
    id=Column(Integer,Primary_key=True,Index=True)
    name=Column(String)
    price=Column(Float)