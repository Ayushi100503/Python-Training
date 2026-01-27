fn = input("Enter the file name: ")
try:
    with open(fn, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")