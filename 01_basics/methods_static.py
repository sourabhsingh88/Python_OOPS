# methods which dont use self param , class level methods

class Student :
    name = "Empty"


    def __init__(self , name , classs):
        self.name = name
        self.classs = classs

    # object level / non static methods
    def print_det(self):
        print(self.name ,self.classs)

    # static methods / belongd to class
    @staticmethod #decorator
    def print_bio(name , age):
        print("hye welcome " , name , age)

s1 = Student("Sourabh" , 12)
s1.print_det()
s1.print_bio("Sourabh" , 20)