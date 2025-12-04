with open("sample.txt", "w") as f:
    f.write("Welcome to my notes. \n")
    f.write("You are doing great.\n")
    f.write("This note was made on 27th november. \n")
    f.write("Little steps make big progress \n")
    f.write("Have a nice day! \n")

with open("sample.txt") as f:
    text = f.read()

chars = len(text)
words = len(text.split())
lines = text.count("\n")+1
print("characters:", chars)
print("words:", words)
print("lines:", lines)