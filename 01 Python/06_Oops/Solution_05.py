class Car:
    def fuel_type(self):
        return "Uses petrol or diesel"

class ElectricCar:
    def fuel_type(self):
        return "Runs on electricity"

def show_fuel_type(vehicle):
    print(vehicle.fuel_type())

my_car = Car()
my_electric_car = ElectricCar()


show_fuel_type(my_car)           
show_fuel_type(my_electric_car)  
