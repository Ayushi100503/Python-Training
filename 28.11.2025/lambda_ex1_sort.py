people = [
    {"name": "Ashi", "age":25},
    {"name": "Riya", "age":32},
    {"name": "Tara", "age":22}
]
sort_people = sorted(people, key= lambda x: x["age"])
print(sort_people)