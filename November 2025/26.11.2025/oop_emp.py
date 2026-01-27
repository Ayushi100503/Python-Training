class Employee:
    def __init__(self,emp_id, name, department, salary):
        self.employee_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary


    def display(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)


e1 = Employee(1,"Ayushi","DET",902000)
e2 = Employee(2,"Sriparna","IT",900000)
e1.display()
print()
e2.display()
print()