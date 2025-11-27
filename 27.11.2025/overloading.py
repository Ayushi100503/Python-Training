class mathops:
    def add(self, a, b=0, c=0):
        return a+b+c
m = mathops()
print(m.add(5))
print(m.add(5, 10))
print(m.add(5, 10, 20))

class Mathops:
    def add(self, *args):
        return sum(args)

n = Mathops()
print(n.add(2))
print(n.add(2, 3))
print(n.add(2, 3, 4))