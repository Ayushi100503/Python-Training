cal_total = lambda qty, price: qty * price
items=[]
for i in range(1,4):
    name = input(f"Enter item{i} name: ")
    qty = int(input(f"Enter quantity: "))
    price = float(input(f"Enter price: "))
    items.append([name, qty, price])

grand_total = sum(cal_total(q, p)for _, q, p in items)
filename = "order_summary.txt"
with open(filename, "w") as f:
    f.write("order summary\n")
    f.write("\n")
    for name, qty, price in items:
        f.write(f"{name} (x{qty}) = Rs{cal_total(qty,price)}\n")
    f.write("\n")
    f.write(f"Grand total: {grand_total}\n")
print(f"{filename} generated successfully")