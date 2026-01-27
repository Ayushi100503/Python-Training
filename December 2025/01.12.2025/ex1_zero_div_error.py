try:
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    result = a/b
    print(result)
except ZeroDivisionError:
    print("Cannot Divide by zero")