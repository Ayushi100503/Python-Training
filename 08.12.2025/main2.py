from flask import Flask, request, jsonify

app = Flask(__name__)

items = ["apple", "banana", "orange"]
#get
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)
#post
@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()
    item = data.get("item")
    items.append(item)
    return "POST EXECUTED"

#put
@app.route("/items/<int:index>", methods=["put"])
def update_item(index):
    data = request.get_json()
    new_value = data.get("item")
    items[index] = new_value
    return "PUT EXECUTED"

#delete
@app.route("/items/<int:index>", methods=["delete"])
def delete_item(index):
    items.pop(index)
    return "DELETE EXECUTED"

if __name__ == "__main__":
    app.run(debug=True)