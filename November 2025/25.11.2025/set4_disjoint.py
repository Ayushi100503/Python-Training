s1 = [1,2,3]
s2 = [4,5,6]
disjoint = True

for i in s1:
    for y in s2:
        if i==y:
            disjoint = False
            break
    if not disjoint:
        break
print("disjoint"if disjoint else "not disjoint")