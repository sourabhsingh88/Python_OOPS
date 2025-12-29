class Vehicle:
    def fuel_type(self):
        print("Generic fuel")

class Car(Vehicle):
    def fuel_type(self):
        print("Petrol or Diesel")

class ElectricCar(Vehicle):
    def fuel_type(self):
        print("Electric")

v1 = Car()
v2 = ElectricCar()

v1.fuel_type()
v2.fuel_type()