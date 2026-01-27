def safe_gen(list, index):
    try:
        return list[index]
    except IndexError:
        print("Index out of range")
nums = [10, 20, 30]
print(safe_gen(nums, 0))
print(safe_gen(nums, 5))