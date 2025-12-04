with open("bigfile.txt", "w") as f:
    f.write("Welcome to my notes. \n")
    f.write("You are doing great.\n")
    f.write("This note was made on 27th november. \n")
    f.write("Little steps make big progress \n")
    f.write("Have a nice day! \n")

with open("bigfile.txt") as f:
    lines = f.readlines()
mid = len(lines)//2
with open("part1.txt", "w") as f1:
    f1.writelines(lines[:mid])
with open("part2.txt", "w") as f2:
    f2.writelines(lines[mid:])
print("files part 1 and part 2 have been made")
