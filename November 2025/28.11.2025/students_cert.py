names = ["Ayushi", "Rohan", "Manish", "Smriti", "Priya", "Rahul"]
with open("students.txt", "w") as f:
    for name in names:
        f.write(f"{name}\n")
with open("students.txt", "r") as f:
    names = [n.strip() for n in f]

make_cert = lambda name: f"Certificate of Completion. \n This is to certify that {name} has successfully completed the course."

for name in names:
       with open(f"certificate_{name}.txt", "w") as c:
           c.write(make_cert(name))

print("Certificates created successfully")
