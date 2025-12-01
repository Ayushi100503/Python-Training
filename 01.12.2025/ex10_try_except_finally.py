filename = "output.txt"
try:
    text = input("Enter text to write: ")
    with open(filename, "w") as file:
        file.write(text)
except PermissionError:
    print("Permission denied")
finally:
    print("Success")