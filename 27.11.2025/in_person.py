class person:
    def __init__(self, name):
        self.name = name

class employee(person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

e = employee("Ayushi", 101)
print(e.name, e.emp_id)
