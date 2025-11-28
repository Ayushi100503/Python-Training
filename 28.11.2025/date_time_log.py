import datetime
log_entry = lambda name, status: f"{datetime.datetime.now()}: {name} | {status}\n"
while True:
    name = input("Name(STOP to end):")
    if name.lower() == "stop":
        break

    status = input("Present/Absent: ")

    with open("attendance_log", "a") as f:
        f.write(log_entry(name, status))
print("Attendance added!")