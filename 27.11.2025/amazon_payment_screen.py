#Amazon payment screen
class payment:
    def pay(self, amount, balance):
        print("Payment Amount: ", amount)
        print("Remaining Balance: ", balance)

class Gpay(payment):
    def pay(self, amount, balance):
        balance -= amount
        print(f"{amount}Paid successfully")
        print("Remaining Balance: ", balance)
        return balance

class Paytm(payment):
    def pay(self, amount, balance):
        balance -= amount
        print(f"{amount}Paid successfully")
        print("Remaining Balance: ", balance)
        return balance

class Phonepe(payment):
    def pay(self, amount, balance):
        balance -= amount
        print(f"{amount} Paid successfully")
        print("Remaining Balance: ", balance)
        return balance

def main():
    print("Welcome to Payment Screen")
    try:
        balance = float(input("Enter your Balance: "))
        amount = float(input("Enter your amount: "))
    except ValueError:
        print("invalid input")
        return

    if amount > balance:
        print("Insufficient balance")

    else:
        print("Current balance is sufficient: ", balance)

    print("Choose Payment Method: ")
    print("1- GPay")
    print("2- Phonepe")
    print("3- Paytm")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Payment Method: GPay")
        method = Gpay()

    elif choice == 2:
        print("Payment Method: Phonepe")
        method = Phonepe()

    elif choice == 3:
        print("Payment Method: Paytm")
        method = Paytm()

    else:
        print("Invalid Choice")
        return
    balance = method.pay(amount, balance)
    print("Payment Completed")
    print("Remaining Balance: ", balance)

if __name__ == "__main__":
    main()