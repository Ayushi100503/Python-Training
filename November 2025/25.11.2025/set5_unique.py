words = ["apple", "banana", "cherry"]
unique = set()
for word in words:
    for char in word:
        unique.add(char)
print(unique)