from datetime import datetime
def log(message):
  with open("log.txt", "a") as f:
      f.write(f"{datetime.now()} - {message}\n")
  with open("log.txt", "r") as f:
      print(f.read())
log("program started")
log("user logged in")