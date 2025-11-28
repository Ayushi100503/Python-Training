import csv

contacts = [
        ["Name", "Phone"],
        ["Rahul, 9988776655"],
        ["Aisha, 9987654321"],
        ["Kabir, 1234567890"]
    ]

with open("contacts.csv","w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(contacts)
print("contacts.csv created")
format_contact = lambda n, p: f"Name:{n}\n Phone:{p}"
with open("contacts.csv") as f:
    reader = csv.DictReader(f)
    with open("contacts_export.txt","w") as out:
        for row in reader:
            name = row["Name"]
            phone = row["Phone"]
            out.write(format_contact(name, phone))
print("contacts_export.txt created")