from flask import Blueprint, jsonify, request
from .controllers import create_new_stock, get_stock_by_id,update_stock_price
from .models import Session, Stock

stock_routes = Blueprint("stocks", __name__)

@stock_routes.route('/',methods=['GET'])
def index():
    session = Session()
    stocks = session.query(Stock).all()

    data = []
    for stock in stocks:
        data.append(
            {
                "id": stock.id,
                "name": stock.name,
                "symbol": stock.ticker_symbol,
                "price": stock.current_price,
            }
        )

    return jsonify(data)

@stock_routes.route('/<int:stock_id>',methods=['GET'])
def get_stock(stock_id):
    try:
        stock = get_stock_by_id(stock_id)
        if stock:
            return jsonify({
                    "id": stock.id,
                    "name": stock.name,
                    "symbol": stock.ticker_symbol,
                    "price": stock.current_price,
                })
        return jsonify({"message": "stock not found"}), 404
    except:
        return jsonify({"message"}), 400
    # Process and return the stock data

@stock_routes.route('/create', methods=['POST'])
def create_stock():
    stock_data = request.get_json()
    try:
        new_stock = create_new_stock(stock_data)
        return jsonify({"message": "Stock Created successfully"}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400


@stock_routes.route("/UpdatePrice", methods=["PUT"])
def update_price():
    try:
        update_stock_price(request.get_json())
        return jsonify({"message": "stock price updated"}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

