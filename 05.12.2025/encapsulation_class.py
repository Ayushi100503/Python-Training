class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
       if amount>0:
          self.__balance += amount
       else:
           print("invalid deposit amount")
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("insufficient funds")
    def get_balance(self):
        return self.__balance
acc = BankAccount("John", 5000)
acc.deposit(2000)
print(acc.get_balance())

acc.withdraw(3000)
print(acc.get_balance())

acc.__balance = 100000 #this will not modify the private balance
print(acc.get_balance())
print(dir(acc))