products = [
    "laptop, 50000",
    "mouse, 1000",
    "keyboard, 2000",
    "monitor, 5000",
    "printer, 3000"
]
with open("products.txt", "w") as f:
    for p in products:
        f.write(p+"\n")
format_line = lambda p, price: f"{p:<15} {price:>5}\n"
with open("products.txt") as f:
    lines = [line.strip() for line in f]

with open("catalog.txt", "w") as c:
    c.write("Product       Price\n")
    c.write("\n")
    for line in lines:
        parts = line.split(",")
        if len(parts) != 2:
            continue
        item, price = parts
        item = item.strip()
        price = price.strip()
        c.write(format_line(item, price))
print("Catalog created")