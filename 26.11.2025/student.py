class student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def total(self):
        return (self.m1 + self.m2 + self.m3)

    def percentage(self):
        return(self.total()/300)*100

    def display(self):
        print("name:", self.name)
        print("marks:", self.total())
        print("percentage:", self.percentage())

s1 = student("Ayushi", 90, 85, 95)
s1.display()