from fileinput import filename

make_letter = lambda name, course:(
    f"Welcome{name}!\n"
    f"We are excited to have you in the {course} course!\n"
    f"Wishing you all the best!\n"
)
def create_welcone_letter(name, course):
    filename = f"Welcome{name}.txt"
    with open(filename, "w") as f:
        f.write(make_letter(name, course))

people = ["Ayushi", "Sriparna", "Ankur", "Tuneer"]
courses = ["Data Scientist", "Machine Learning", "Python","Web Development"]
for name, course in zip(people, courses):
    create_welcone_letter(name, course)
print("welcome letters created successfully")