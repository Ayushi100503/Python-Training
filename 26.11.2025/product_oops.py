class Product:
    def __init__(self,attribute_name, price, quantity):
        self.attribute_name = attribute_name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return (self.price * self.quantity)

    def display(self):
        print(self.attribute_name)
        print(self.price)
        print(self.quantity)
        print(self.total_cost())

p1= Product("laptop", 90000, 5)
p1.display()