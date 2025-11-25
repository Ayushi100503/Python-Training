s1 = [1,2,3,5]
s2 = [3,4,5,6]
result=[]
for x in s1:
    if x not in s2:
      result.append(x)

for x in s2:
    if x not in s1:
        result.append(x)

print(result)