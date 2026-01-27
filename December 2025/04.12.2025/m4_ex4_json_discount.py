import json
product = [
    {"id":1, "name": "Chocolate Cake", "price": 5000},
    {"id":2, "name": "laptop", "price": 90000},
    {"id":3, "name": "Apple", "price": 100},
    {"id":4, "name": "Banana", "price": 200}
]

with open("product.json", "w") as f:
    json.dump(product, f, indent=4)
with open("product.json") as f:
    product = json.load(f)
for p in product:
    p["discount_price"] = round(p["price"]*0.9,2)
with open("product.json", "w") as f:
    json.dump(product, f, indent=4)
print("updated products saved to json")