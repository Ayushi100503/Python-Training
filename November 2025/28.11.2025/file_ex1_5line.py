with open("notes.txt", "w") as f:
    f.write("Welcome to my notes. \n")
    f.write("You are doing great.\n")
    f.write("This note was made on 27th november. \n")
    f.write("Little steps make big progress \n")
    f.write("Have a nice day! \n")

with open("notes.txt", "r") as f:
    content = f.read()
    print(content)