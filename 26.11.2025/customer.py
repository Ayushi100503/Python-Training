class customer:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def is_eligble(self):
        return self.age > 25

c1 = customer("Ayushi", 25, "California")
c2= customer("Jyoti", 28, "Delhi")
print(c1.is_eligble())
print(c2.is_eligble())