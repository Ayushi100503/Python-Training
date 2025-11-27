from datetime import datetime
with open("log.txt", "w") as f:
    f.write(f"{datetime.now()}")

print("Contents of log.txt are:")

with open("log.txt", "r") as f:
    print(f.read())
