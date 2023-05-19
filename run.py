from app import app

app.config.from_object('config')
from app.routes import stock_routes
app.register_blueprint(stock_routes)


if __name__ == "__main__":
    app.run(debug=True)