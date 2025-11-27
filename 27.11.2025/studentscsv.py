import csv

students = [
    ["Ayushi", 98],
    ["Alice",82],
    ["Bob", 70],
    ["Charlie", 78],
]
with open("students.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(students)

print("Done")
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    print(students)