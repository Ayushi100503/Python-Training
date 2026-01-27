path = input("Please enter the file path: ")
try:
    text = input("Enter text to write: ")
    with open(path, "w") as f:
        f.write(text)
except FileNotFoundError:
    print("File not found")
finally:
    print("Success")
