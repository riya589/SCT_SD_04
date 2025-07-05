# app.py
from flask import Flask, render_template, jsonify
from scraper import get_products

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/products')
def api_products():
    products = get_products()
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
