class payment:
    def process(self):
        print("Processing payment")

class CreditCardPayment(payment):
    def process(self):
        print("Processing credit card payment")

class UPIPayment(payment):
    def process(self):
        print("Processing UPI payment")

p1 = CreditCardPayment()
p1.process()

p2 = UPIPayment()
p2.process()