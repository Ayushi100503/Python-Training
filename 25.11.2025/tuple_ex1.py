t = (1, "python", 2, "java", 3, "c++", 4)
numbers = ()
strings = ()
for i in t:
    if type(i)==str:
        numbers = numbers + (i,)
    else:
        strings = strings + (i,)
print(numbers)
print(strings)