with open("python.txt", "w") as f:
    f.write("Hello, this is first line. \n")
    f.write("This file was created using Python. \n")
    f.write("Python is easy. \n")

with open("python.txt", "r") as f:
    for line in f:
        if "Python" in line:
            print(line)
