class student:
    def __init__(self,sid, name,marks):
        self.sid = sid
        self.name = name
        self.marks = marks
    def grades(self):
        if self.marks>=90:
            return 'A'
        elif self.marks>=75:
            return 'B'
        elif self.marks>=60:
            return 'C'
        else:
            return 'D'
s = student(1, "Ayushi", 98)
print(s.name, "Grade:", s.grades())