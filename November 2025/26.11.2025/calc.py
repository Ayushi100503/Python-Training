class calculator:
    def __init__(self, value=0):
        self.value = 0
    def add(self, num1, num2):
        self.value = num1 + num2
        return self.value
    def sub(self, num1, num2):
        self.value = num1 - num2
        return self.value
    def mul(self, num1, num2):
        self.value = num1 * num2
        return self.value
    def div(self, num1, num2):
        if num2!=0:
            self.value = num1 / num2
        else:
            return ("error")
        return self.value
    def reset(self):
        self.value = 0
        return self.value


calc = calculator()
print("initial value: ", calc.value)
print("add 30+20: ", calc.add(30,20))
print("sub 50-20: ", calc.sub(50,20))
print("mul 30*5: ", calc.mul(30,5))
print("div by 6/3: ", calc.div(6,3))
print("reset value: ", calc.reset())
