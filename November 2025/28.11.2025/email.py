with open("names.txt", "w") as f:
    f.write("Rahul\n")
    f.write("Aisha\n")
    f.write("Kabir\n")
    f.write("Meera\n")
print("names.txt created")
make_email = lambda name:(
    f"Dear{name},\n"
    f"Your training session starts tomorrow.\n",
    f"Regards.\n",
    f"Training Team\n"
)
with open("names.txt") as f:
    names = [n.strip() for n in f]
for name in names:
    filename = f"email_{name}.txt"
    with open(filename, "w") as mail:
        mail.write(f"{make_email(name)}\n")
print("email templates generated")