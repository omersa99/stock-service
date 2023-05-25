
from sqlalchemy import Column, ForeignKey, Integer,DateTime, String,Float, create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import current_app

import datetime

engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI_INTERNAL'])
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Stock(Base):
    __tablename__ = "stocks"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    ticker_symbol = Column(String(20))
    current_price = Column(Float)

class PriceData(Base):
    __tablename__ = "PriceData"
    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stocks.id'), nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<PriceData stock_id={self.stock_id}, price={self.price}, timestamp={self.timestamp}>'


Base.metadata.create_all(engine)

