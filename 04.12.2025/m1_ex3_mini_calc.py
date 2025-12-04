def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return "error division by 0" if b == 0 else a/b

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
op = input("Enter operation: ")
if op == "+":
    print(add(a,b))
elif op == "-":
    print(sub(a,b))
elif op == "*":
    print(mul(a,b))
elif op == "/":
    print(div(a,b))
else:
    print("invalid operation")