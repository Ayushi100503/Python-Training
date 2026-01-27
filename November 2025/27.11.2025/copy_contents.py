with open("source.txt", "w") as f:
    f.write("Hello, this is first line. \n")
    f.write("This file was created using Python. \n")

print("Source file was created successfully.")

with open("source.txt", "r") as f, open("backup.txt", "w") as b:
    b.write(f.read())

print("Content copied to backup file successfully.")