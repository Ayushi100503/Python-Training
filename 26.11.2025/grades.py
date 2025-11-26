class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total(self):
        return (self.m1 + self.m2 + self.m3)

    def percentage(self):
        return(self.total()/300)*100

    def grade(self):
        p = self.percentage()
        if p >= 90:
            return "A"
        elif p >= 80:
            return "B"
        elif p >= 70:
            return "C"
        else:
            return "D"

    def display(self):
        print("name:", self.name)
        print("marks:", self.total())
        print("percentage:", self.percentage())
        print("grade:", self.grade())

s2 = Student("Ayushi", 90, 85, 90)
print("total:", s2.total())
print("percentage:", s2.percentage())
print("grade:", s2.grade())
s2.display()
