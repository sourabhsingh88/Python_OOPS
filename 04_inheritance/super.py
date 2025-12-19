class Car:

    def __init__(self , type):
        self.type = type


    def start(self):
         print(self.type , "car Started")


    def stop(self):
         print(self.type  ,"car Stopedd")


class Fortuner(Car) :
    def __init__(self, model , type):
        super().__init__(type)  # Access parent
        self.model = model
        super().start()
    def offroad(self):
        print(self.model, "Model" , self.type ,"Car" ,"on off roads")

c1 =Fortuner(2018,"Petrol")
c1.offroad()

