student = {
    "name":"ayushi",
    "age":22,
    "city":"kolkata"
}
print(student["name"])
print(student["age"])

print(student.get("name"))
student["email"] ="test@example.com"
student["city"] ="gangtok"
print(student)
student.pop("age")
del student["city"]
student.clear()
print(student)



for k in student.keys():
    print(k)
for v in student.values():
    print(v)
for k,v in student.items():
    print(k,v)