class temperature:
    def __init__(self, value):
        self.value = value

    def f(self):
        return (self.value*9/5)+32
    
    def c(self):
        return(self.value-32)*5/9
    
    def display(self):
        print("Celsius to Fareneheit:", self.c())
        print("Farenheit to Celsius:", self.f())

t = temperature(50)
t.display()
