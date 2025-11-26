balance = 100000
class BankAccount:
    def __init__(self, owner):
        self.owner = owner

    def deposit(self, amount):
        global balance
        balance += amount
        print(self.owner, "deposited ", amount)

    def withdraw(self, amount):
        global balance
        if amount > balance:
            print("Not enough money")
        else:
            balance -= amount
            print(self.owner, "withdrawn ", amount)
my_account = BankAccount("My Account")
my_account.deposit(50000)
my_account.withdraw(20000)
print(balance)
