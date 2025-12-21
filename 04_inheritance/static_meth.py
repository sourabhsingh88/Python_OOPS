class Car:
    @staticmethod
    def validate_type(car_type):
        return car_type in ["Petrol", "Diesel", "Electric"]


a = Car.validate_type("Petrol")
print(a) #True

b = Car.validate_type("CNG")
print(b) #False