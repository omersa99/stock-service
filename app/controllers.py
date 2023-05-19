from flask import jsonify
from .models import Session, Stock

def get_stock_by_id(stock_id):
    session = Session()
    stock = session.query(Stock).get(stock_id)
    if stock:
        return stock
    return None

def create_new_stock(stock_data):

    name = stock_data.get('name')
    ticker_symbol = stock_data.get('ticker_symbol')
    current_price = stock_data.get('current_price')

    # Validate the data
    if not name or not ticker_symbol or not current_price :
        raise ValueError("Invalid Stock data. Please provide all required fields.")

    newStock = Stock(name=name,ticker_symbol=ticker_symbol,current_price=current_price)

    session = Session()
    session.add(newStock)
    session.commit()



def update_stock_price(stock_data):
    session = Session()
    stock_id = stock_data.get('id')
    new_price = stock_data.get('price')
        # Validate the data
    if not stock_id or not new_price:
        raise ValueError("Invalid Stock data. Please provide Valied ID.")


    current_stock = session.query(Stock).filter(Stock.id == stock_id).one()
    current_stock.current_price = new_price
    session.commit()
    return jsonify({"status": "success"})
