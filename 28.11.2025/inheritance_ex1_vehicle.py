class vehicle:
    def start(self):
        print("vehicle starts")

class car(vehicle):
    def start(self):
        print("Car engine starts")
c = car()
c.start()