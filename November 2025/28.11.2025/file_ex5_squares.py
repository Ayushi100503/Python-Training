with open("squares.txt", "w") as f:
    for number in range (1,21):
        f.write(f"{number**2}\n")

with open("squares.txt", "r") as f:
    content = f.read()
    print(content)