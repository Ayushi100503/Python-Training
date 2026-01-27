class mobile:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

m = mobile("Samsung", "A52")
m.display()