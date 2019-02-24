from sqlalchemy import create_engine
from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///shop.sqlite', echo=True)
Base = declarative_base()

class Shop(Base):
    __tablename__ = 'Shop'

    id = Column('code_id', Integer, primary_key=True)
    category = Column('category', String)
    title = Column('title', String)
    price = Column('price', String)

    def __init__(self, category, title,price):
        """"""
        self.category = category
        self.title = title
        self.price=price



# create tables
Base.metadata.create_all(engine)