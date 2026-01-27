nums = [5, 2, 7, 5, 9, 5, 3]
value = int(input("enter value to find: "))
indices=[]
for i in range(len(nums)):
    if nums[i] == value:
        indices.append(i)
print("indices", indices)