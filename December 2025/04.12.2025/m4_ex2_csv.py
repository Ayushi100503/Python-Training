import csv
employees = [
    {"id":i, "name":f"Emp{i}", "salary":30000+i*1000}
    for i in range(1,21)
]
with open("employees.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id","name","salary"])
    writer.writeheader()
    writer.writerows(employees)

with open("employees.csv") as f:
    reader = csv.DictReader(f)
    data = list(reader)

print(data)