from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []

@app.route("/")
def home():
    return "SpyHostTool API Running"

@app.route("/order", methods=["POST"])
def order():
    data = request.json

    orders.append({
        "user": data["user"],
        "plan": data["plan"],
        "status": "pending"
    })

    return jsonify({
        "message": "Order received",
        "status": "pending"
    })

@app.route("/orders")
def get_orders():
    return jsonify(orders)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)