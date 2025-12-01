items = ["10", "abc", "225", "banana", "50", "18"]
for item in items:
    try:
        print(int(item))
    except ValueError:
        print(f"cannot convert {item} to integer")