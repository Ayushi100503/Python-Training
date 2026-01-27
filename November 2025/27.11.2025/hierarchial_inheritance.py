class vehicle:
    def __init__(self,name, brand, speed):
        self.name = name
        self.brand = brand
        self.speed = speed

class car(vehicle):
    def __init__(self, name, brand, speed, model):
        super().__init__(name, brand, speed)
        self.model = model

class bike(vehicle):
    def __init__(self, name, brand, speed, type):
        super().__init__(name, brand, speed)
        self.type = type

c1 = car("Name: Car","Brand: BMW", "Speed: 100", "Model: M34i")
b1 = bike("Name: Bike","Brand: KTM", "Speed: 200", "Type: Sports")
print(c1.name, c1.brand, c1.speed, c1.model)
print(b1.name, b1.brand, b1.speed, b1.type)

class shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class circle(shape):
    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.radius = radius

class rectangle(shape):
    def __init__(self, name, color, length, width):
        super().__init__(name, color)
        self.length = length
        self.width = width

c = circle("Name: Circle", "Color: Purple", "Radius: 18")
r = rectangle("Name: Rectangle","Color: Blue", "Length: 20", "Width: 80")
print(c.name, c.color, c.radius)
print(r.name, r.color, r.length, r.width)
