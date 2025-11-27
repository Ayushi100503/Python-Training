with open("numbers.txt", "w") as f:
    for number in range (1,11):
        f.write(f"{number**2}\n")

with open("numbers.txt", "r") as f:
    content = f.read()
    print(content)