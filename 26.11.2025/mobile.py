class mobile:
    def __init__(self,brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def upgrade_storage(self,extra_storage):
        self.storage += extra_storage
        print("storage upgraded", self.storage)

m = mobile("samsung", "a52", 128)
m.upgrade_storage(256)