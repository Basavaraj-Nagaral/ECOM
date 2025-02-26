from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return [
    { id: 1, "name": "Fresh Tomatoes", "price": 30, "image": "https://via.placeholder.com/150", "category": "Vegetables" },
    { id: 2, "name": "Organic Carrots", "price": 40, "image": "https://via.placeholder.com/150", "category": "Vegetables" },
    { id: 3, "name": "Green Apples", "price": 100, "image": "https://via.placeholder.com/150", "category": "Fruits" },
    { id: 4, "name": "Brown Bread", "price": 50, "image": "https://via.placeholder.com/150", "category": "Bakery" },
    { id: 5, "name": "Fresh Milk", "price": 60, "image": "https://via.placeholder.com/150", "category": "Dairy" }
  ]

@app.route('/api', methods=['GET'])
def api():
    return jsonify({"message": "Hello, this is the API endpoint!"})

if __name__ == '__main__':
    app.run(debug=True)
