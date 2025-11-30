lst = [1,2,3,4,5,6,7,8,9]
n = 2
n = n%len(lst)
rotated = lst[-n:]+lst[:-n]
print(rotated)