class camera:
    def __init__(self, megapixel):
        self.megapixel = megapixel

class phone:
    def __init__(self, number):
        self.number = number

class smartphone(camera, phone):
    def __init__(self, megapixel, number, brand):
        camera.__init__(self, megapixel)
        phone.__init__(self, number)
        self.brand = brand

s = smartphone("megapixel: 108", "number: 9163867891", "brand: Nothing")
print( s.megapixel, s.number, s.brand)
