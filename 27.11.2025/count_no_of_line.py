count = 0
with open("notes.txt", "r") as f:
    for line in f.readlines():
        count = count + 1

print("Number of lines in notes.txt: ", count)
