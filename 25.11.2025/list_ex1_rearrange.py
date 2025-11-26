l = [1,-9,-8,7,8,-2,4,-5,3]
l1 = []
l2 = []
for i in l:
    if i>0:
        l1.append(i)
    else:
        l2.append(i)
print(l1+l2)