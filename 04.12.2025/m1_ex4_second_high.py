num = int(input("How many numbers would you like? "))
numbers = tuple(int(input(f"Enter number {i+1}: ")) for i in range(num))
largest = max(numbers)
second = None
for n in numbers:
    if n!=largest:
        if second is None or n>second:
           second = n
print(second)
