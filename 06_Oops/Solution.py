class Car:
    count = 0  # Class variable to track cars

    def __init__(self, model):
        self._model = model
        Car.count += 1

    def fuel_type(self):
        return "Uses petrol or diesel"

    @staticmethod
    def general_description():
        return "Cars usually have four wheels and can run on various types of fuel."

    @property
    def model(self):
        return self._model

class Battery:
    def battery_info(self):
        return "Battery capacity is 100 kWh."

class Engine:
    def engine_info(self):
        return "Electric motor with instant torque."

class ElectricCar(Car, Battery, Engine):
    def fuel_type(self):
        return "Runs on electricity"

# Test everything
my_car = Car("Toyota Corolla")
my_tesla = ElectricCar("Tesla Model S")

print(my_car.fuel_type())                  # Uses petrol or diesel
print(my_tesla.fuel_type())                # Runs on electricity

print(Car.count)                           # 2

print(Car.general_description())           # Static method

print(my_car.model)                        # Read-only access
# my_car.model = "New Model"              # Would raise an error if tried

print(isinstance(my_tesla, ElectricCar))   # True
print(isinstance(my_tesla, Car))           # True

print(my_tesla.battery_info())             # From Battery class
print(my_tesla.engine_info())              # From Engine class
