class animal:
    def sound(self):
        print("Animal makes sound.")

class cat(animal):
    def sound(self):
        print("Cat meows.")

class dog(animal):
    def sound(self):
        print("Dog barks.")

for animal in (cat(), dog()):
    animal.sound()