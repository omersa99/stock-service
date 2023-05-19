from sqlalchemy import Column, Integer, String,Float, create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import current_app

engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI_INTERNAL'])
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Stock(Base):
    __tablename__ = "stocks"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    ticker_symbol = Column(String(20))
    current_price = Column(Float)
Base.metadata.create_all(engine)

