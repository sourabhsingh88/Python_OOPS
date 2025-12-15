class Student :

    school = "SAM"

    def __init__(self , name  , classs) :
        self.name = name
        self.classs = classs

    #Non static methods
    def std_detail(self):
        print("Welcome",self.school , self.name , self.classs)
    def get_marks(self):
        print("Class is " , self.classs)

#Non static method dont work in class we need to use self keyword
#If we want to use we need to use annpotation @staticmethod
    @staticmethod
    def welcome():
        print("hye wellcome")

s1 = Student("sourabh" , 12)
s1.std_detail()
s1.get_marks()
s1.welcome()