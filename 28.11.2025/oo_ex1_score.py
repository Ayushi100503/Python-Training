class score:
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return score(self.value + other.value)
    
    def __gt__(self, other):
        return self.value>other.value
    
s1 = score(50)
s2 = score(20)
s3 = s1+s2
print("Combined score: ", s3.value)
print("Is s1>s2?", s1>s2)