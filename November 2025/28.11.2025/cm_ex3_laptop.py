class laptop:
    def __init__(self,brand, RAM, price):
        self.brand = brand
        self.RAM = RAM
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("RAM:", self.RAM)
        print("Price:", self.price)

l = laptop("Apple", "M4 chip", 90000)
l.display()