class bankaccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.logs = []

    def deposit(self, amount):
        self.balance += amount
        self.logs.append(f"deposited {amount}")
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            self.logs.append(f"withdraw failed {amount}")
            return "insufficient balance"
        else:
            self.balance -= amount
            self.logs.append(f"withdraw {amount}")
            return self.balance

    def check_balance(self):
        return self.balance

    def show_logs(self):
        for log in self.logs:
            print(log)

a = bankaccount("Ayushi",100000)
a.deposit(1200)
a.withdraw(100)
print(a.check_balance())
a.show_logs()