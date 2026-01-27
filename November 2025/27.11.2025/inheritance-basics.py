class Animal:
    def speak(self):
        print("animal makes sound")

class Dog(Animal):
    def bark(self):
        print("dog barks")

d = Dog()
d.speak()
d.bark()
