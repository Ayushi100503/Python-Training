import csv
orders = [
    {"item":"Apple", "quantity":5, "price":80},
    {"item":"Banana", "quantity":2, "price":10},
    {"item": "Orange", "quantity":3, "price":15}
]
with open("orders.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["item", "quantity", "price"])
    writer.writeheader()
    writer.writerows(orders)
print("orders.csv created successfully")

cal_total = lambda quantity, price: quantity * price
total = 0
with open("orders.csv", "r") as f:
    reader = csv.DictReader(f)
    with open("invoice.txt", "w") as inv:
        for row in reader:
            item = row["item"]
            quantity = int(row["quantity"])
            price = float(row["price"])
            line_total = cal_total(quantity, price)
            total += line_total
            inv.write(f"{item}(x{quantity})-Rs{line_total}\n")
        inv.write("\n")
        inv.write(f"Grand Total; Rs{total}\n")
print("invoice created successfully")

