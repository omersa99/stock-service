from flask import jsonify
from .models import PriceData, Session, Stock

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

    # Add a new record to the price data table
    price_data = PriceData(stock_id=stock_id, price=new_price)
    session.add(price_data)

    current_stock = session.query(Stock).filter(Stock.id == stock_id).one()
    current_stock.current_price = new_price
    session.commit()
    return jsonify({"status": "success"})

# This endpoint retrieves the price data for the specified stock
# , sorts it by timestamp, and converts it to a Plotly-compatible format.
# We can then use a JavaScript library like Plotly.js to create a chart on
# the front-end.

# @app.route('/stocks/<int:stock_id>/chart')
# def stock_chart(stock_id):
#     # Retrieve the price data for the stock
#     price_data = session.query(PriceData).filter(PriceData.stock_id == stock_id).all()

#     # Convert the price data to a list of (timestamp, price) tuples
#     data = [(pd.timestamp, pd.price) for pd in price_data]

#     # Sort the data by timestamp
#     data = sorted(data, key=lambda x: x[0])

#     # Convert the data to a Plotly-compatible format
#     chart_data = {
#         'x': [d[0] for d in data],
#         'y': [d[1] for d in data],
#         'type': 'scatter',
#         'mode': 'lines+markers'
#     }

#     return jsonify(chart_data)