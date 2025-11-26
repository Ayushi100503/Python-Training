class student:
    pass
a=student()
b=student()

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1 = Student("Ayushi",22)
s2 = Student("James",23)
print(s1.name,s1.age)
print(s2.name,s2.age)