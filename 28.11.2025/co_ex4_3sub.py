class student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def percentage(self):
        total = self.m1 + self.m2 + self.m3
        return(total/300)*100
    
s = student(87, 89, 90)
print(s.percentage())