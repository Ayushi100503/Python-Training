Sets = {2, 4, 6, 8, 10}
Target = 12
pairs = []

for x in Sets:
     for y in Sets:
         if x<=y and x+y==Target:
             pairs.append((x,y))
print(pairs)