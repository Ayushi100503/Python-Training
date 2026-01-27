class company:
    def work(self):
        print("work")

class employee(company):
    def __init__(self, name, age):
        self.name = name
        self.age = age

e = employee("name: Ayushi", 22)
e.work()
print(e.name, e.age)


class vehicle:
    def honk(self):
        print("vehicle honks")

class car(vehicle):
    def __init__(self, brand):
        self.brand = brand

c = car("BMW")
c.honk()
print(c.brand)