try:
    num = int(input("Enter number: "))
    print(10/num)
except ValueError:
    print("invalid number")
except ZeroDivisionError:
    print("cannot divide by zero")