class Student:
    def __init__(self , pub , private):
        self.pub = pub
        self.__private = private

    def set_private(self , num ):
        self.__private = num

    def get_pvt(self):
        return self.__private

s1 =Student(1 , 10)
print(s1.pub)
# print(s1.private) #Not access
s1.set_private(25)
print(s1.get_pvt()) #accessable