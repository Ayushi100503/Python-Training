print("hello world!")

name = "Ayushi"
age = 22
salary = 4.6
print(name)
print(age)
print(salary)


a = 10
b = 3
print("addition: ", a+b)
print("division: ", a/b)
print("floor division: ", a//b)
print("modulus: ", a%b)
print("power: ", a**b)


for a in range(1,21):
    if a%2==0:
       print(a, "is even");
    else:
       print(a, "is odd")


marks = int(input("enter your score: "))
if marks >= 90:
    print("grade A")
elif marks >= 75:
    print("grade B")
elif marks >= 60:
    print("grade C")
else:
    print("grade D")


for i in range(1,6):
 print("number is", i)


counter = 1
while counter <= 5:
    print("Count: ", counter)
    counter += 1 #same as counter = counter + 1


for i in range(10):
    if i==5:
        break
    print(i)
    
for i in range(10):
    if i%2==0:
        continue
    print(i)
