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

s = smartphone("megapixel: 108", "number: 9163867891", "brand; Nothing")
print( s.megapixel, s.number, s.brand)

class programmer:
    def __init__(self, language):
        self.language = language


class statistician:
    def __init__(self, methods):
        self.methods = methods

class data_scientist(programmer, statistician):
    def __init__(self, language, methods, experience):
        programmer.__init__(self, language)
        statistician.__init__(self, methods)
        self.experience = experience

d = data_scientist("language: Python", "methods: Time series", "experience: 5+ years")
print(d.language, d.methods, d.experience)





