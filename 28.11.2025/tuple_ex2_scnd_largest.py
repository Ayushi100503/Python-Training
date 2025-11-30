num =(10, 20, 30, 40, 50, 60, 70, 80, 90)
largest = max(num)
second = None
for n in num:
    if n!=largest:
        if second is None or n>second:
           second = n
print(second)