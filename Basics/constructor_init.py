class Car :
    name = "Sourabh"

    #below is constructor which initilize the object
    # and it auto evocked when object is crated
    def __init__ (self , name , color) :
        #Self points to currect object whic is created
        print("Cunstructor Invoked")
        self.name = name
        self.color = color


c1 =  Car("Ram" , "Black")
print(c1.name , c1.color)