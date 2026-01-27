emp = {
"e1": {"dept": "IT"},
"e2": {"dept": "HR"},
"e3": {"dept": "IT"},
}
dept_count = {}
for e in emp:
    dept = emp[e]["dept"]
    if dept not in dept_count:
        dept_count[dept] = 1
    else:
        dept_count[dept] += 1
print(dept_count)