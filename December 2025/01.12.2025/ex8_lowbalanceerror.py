class LowBalanceError(Exception):
    pass
def withdraw(amount, balance):
    if amount>balance:
        raise LowBalanceError("Insufficient funds")
    return balance-amount
s = withdraw(100, 1000000)
print(s)
#m = withdraw(100, 10)
#print(m)