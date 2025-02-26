from flask import Flask, jsonify, request
import os

port = int(os.environ.get("PORT", 5000))
app = Flask(__name__)

@app.route('/product', methods=['GET'])
def home():
    return jsonify([
    { "id": 1, "name": "Fresh Tomatoes", "price": 30, "category": "Vegetables" },
    { "id": 2, "name": "Organic Carrots", "price": 40, "category": "Vegetables" },
    { "id": 3, "name": "Green Apples", "price": 100, "category": "Fruits" },
    { "id": 4, "name": "Brown Bread", "price": 50, "category": "Bakery" },
    { "id": 5, "name": "Fresh Milk", "price": 60, "category": "Dairy" }
  ])

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if username == "admin" and password == "admin123":
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=port, debug=True)