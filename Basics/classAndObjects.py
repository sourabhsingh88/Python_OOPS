class student :
    name = "sourabh"

print(student.name) #By class name
s1 = student() #Creating Object
print(s1.name)


class Car :
    name = "Sourabh" # Class variable
    def __init__ (self , name , color) :
        self.name = name #Instance Variable
        self.color = color


c1 =  Car("Ram" , "Black")
print(c1.name , c1.color)