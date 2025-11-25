fruits = ["apple", "mango", "litchi", "cherry"]
fruits[2] = "kiwi"
print(fruits)

fruits.append("grapes")
print(fruits)

fruits.insert(1,"orange")
print(fruits)

fruits.remove("kiwi")
print(fruits)

fruits.pop()
print(fruits)

fruits.pop(1)
print(fruits)

del fruits[0]
print(fruits)