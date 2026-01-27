try:
    f = open("data.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("file not found")
finally:
    print("closing operation completed")