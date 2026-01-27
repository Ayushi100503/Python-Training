a = int(input("enter number: "))
temp = a
rev = 0
while a>0:
    remainder = a%10
    rev = (rev*10)+remainder
    a = a//10
print(rev)