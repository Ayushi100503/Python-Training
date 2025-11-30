class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length + self.width)
    
r = rectangle(10,5)
print(r.area(), r.perimeter())