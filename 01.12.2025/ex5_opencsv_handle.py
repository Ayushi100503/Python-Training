import csv
filename = input("Enter file name: ")
try:
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File not found")
except  csv.Error:
    print("Incorrect file format")