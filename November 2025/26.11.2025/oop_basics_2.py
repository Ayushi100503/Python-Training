class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("brand: ", self.brand)
        print("model: ", self.model)
        print("price: ", self.price)

car1 = Car("Toyota", "Fortuner", 20000)
car2 = Car("Hyundai", "Creta", 890000)
car3 = Car("Tesla", "Model 3", 4520000)
car1.display()
print()
car2.display()
print()
car3.display()