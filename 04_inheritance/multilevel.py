class Vehicle :
    def __init__(self , type) :
        self.type= type

    def start(self):
        print(self.type ,"Vehicle Started")

    def stop(self ):
        print(self.type , "vehicle stoped")

class Car(Vehicle) :

    def music(self ):
        print("Playing Music in car")

class Toyoto(Car) :


    def offroad(self ):
        print("offroading")


c1 = Toyoto("Petrol")
c1.start() # access to super parent class
c1.music() # access to parent class
c1.offroad() # access to current class