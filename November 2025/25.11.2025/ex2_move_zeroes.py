num = [0, 3, 0, 5, 7, 0, 9]
result = []
count = []
for n in num:
    if n!=0:
        result.append(n)
    else:
        count.append(n)

final = result + count
print(final)