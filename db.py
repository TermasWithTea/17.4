from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///taskmanenger.db', echo = True)

sessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass