def calculate_total(a, b):
    total = a + b
    print("Debug: a =", a)
    print("Debug b=", b)
    print("Debug Total =", total)
    result = total/0
    print("Result =", +result)

calculate_total(20, 10)