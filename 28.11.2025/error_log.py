import datetime
log_error = lambda msg:(f"{datetime.datetime.now()} - ERROR - {msg}\n")
def write_error(msg):
    with open("error.log", "a") as f:
        f.write(log_error(msg))
for i in range(1,6):
    write_error(f"Sample error number {i}")
print("5 errors logged")