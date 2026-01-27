class person:
    def __init__(self, name):
        self.name = name


class employee(person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

class manager(employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

m = manager("name: Manish", "emp_id: 123", "department: IT")
print(m.name, m.emp_id, m.department)

class device:
    def __init__(self, brand):
        self.brand = brand

class computer(device):
    def __init__(self, brand, processor):
        super().__init__(brand)
        self.processor = processor

class laptop(computer):
    def __init__(self, brand, processor, model):
        super().__init__(brand, processor)
        self.model = model

l = laptop("brand: Apple", "processor: ARMv9", "model: Air M4")
print(l.brand, l.processor, l.model)



