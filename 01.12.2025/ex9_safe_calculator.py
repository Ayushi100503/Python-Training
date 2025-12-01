def calculator(a, b, op):
    try:
        a = float(a)
        b = float(b)
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            return "Invalid operation"
    except ValueError:
        return "Invalid value"
    except ZeroDivisionError:
        return "Cannot divide by zero"
print(calculator(20, 10, "*"))
print(calculator(20, 10, "+"))
print(calculator(20, 10, "-"))
print(calculator(20, 0, "/"))
print(calculator("sad", 10, "*"))