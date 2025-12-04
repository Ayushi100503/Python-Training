employees = {
    "Amit":55000,
    "Bob":72000,
    "Charlie":65000,
    "John":85000,
    "Kevin":45000,
}
high_salary = {name:sal for name,sal in employees.items() if sal>60000}
print(high_salary)