nums = [23, 89, 12, 78, 55, 42]
max1 = max2 = -1

for n in nums:
    if n>max1:
        max1 = max2
        max1 = n
    elif n>max2 and n!= max1:
        max2 = n
print("second largest is: ",max2)