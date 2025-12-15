class Car:
    def __init__(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name

tesla = Car("tesla")

print(tesla.get_name())