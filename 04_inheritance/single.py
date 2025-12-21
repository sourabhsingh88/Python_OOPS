class Car:

    def __init__(self , type):
        self.type = type
    def start(self):
         print(self.type , "car Started")

    def stop(self):
         print(self.type  ,"car Stopedd")


class Fortuner(Car) :
    def __init__(self, model , type):
        self.model = model
        super().__init__(type)
    def offroad(self):
        print(self.model , self.type ,"on off roads")

c1 =Fortuner(20018,"Petrol")
c1.start()
c1.stop()
c1.offroad()