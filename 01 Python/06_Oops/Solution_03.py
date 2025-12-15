class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model


class ElectriCar(Car):
    def __init__(self, name, model, battary_size):
        super().__init__(name, model)
        self.battary_size = battary_size

    def fuel_type(self):
        return "Electric charge"
    


tesla = ElectriCar("tesla", "model s", "66KW")

print(tesla.fuel_type())






