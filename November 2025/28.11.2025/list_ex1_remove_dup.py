num = [1,2,3,4,5,6,2,5,6]
unique_list = []
for n in num:
    if n not in unique_list:
        unique_list.append(n)
print(unique_list)