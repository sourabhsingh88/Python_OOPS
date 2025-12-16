from abc import ABC , abstractmethod

class Car(ABC) :

    def __init__(self, name, model):
        self.name = name
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def carDetail(self):
        print("name is " , self.name , "and model is " , self.model)


class PetrolCar(Car) :
    def start(self):
        print("Petrol Car Started")

    def stop(self):
        print("Petrol Car Stoped")

class ElcCar(Car) :
    def start(self):
        print("Elc Car Started")

    def stop(self):
        print("Elc Car Stoped")



c1 = PetrolCar("Verna" , 2025)
c1.start()
c1.stop()
c1.carDetail()

c2 = ElcCar("Verna2121" , 2202)
c2.start()
c2.stop()
c2.carDetail()


