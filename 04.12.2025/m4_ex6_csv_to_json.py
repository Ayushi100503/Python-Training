import csv, json
with open("data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "price"])
    writer.writeheader()
    writer.writerows([
        {"id": 1, "name": "mobile", "price": 50000},
        {"id": 2, "name": "apple", "price": 500},
        {"id": 3, "name": "banana", "price": 400},
        {"id": 4, "name": "laptop", "price": 90000}
    ])
with open("data.csv") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
with open("data.json", "w") as f:
    json.dump(rows, f, indent=4)
print("csv created and converted to json")


