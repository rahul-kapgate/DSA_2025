# class MyClass():
#     name = "Rahul"


# Person = MyClass()

# print(Person.name)


class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def CarInfo(self):
        print(self.name,"-", self.model)     


tesla = Car("Tesla", "maodel s")


# print(tesla.name, tesla.model)
tesla.CarInfo()