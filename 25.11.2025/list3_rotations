lst = [1,2,3,4,5,6,7,8,9]
n=2
length = len(lst)
n=n%length
print(lst)

for i in range(n):
    last = lst[-1]
    for i in range(length-1,0,-1):
        lst[i] = lst[i-1]
    lst[0]=last
print(lst)
