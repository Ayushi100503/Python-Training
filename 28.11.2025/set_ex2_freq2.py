num = [1,2,2,3,4,4,4,5]
seen = set()
twice = set()
for n in num:
    if n not in seen:
        seen.add(n)
    elif n in seen:
        twice.add(n)
print(list(twice))