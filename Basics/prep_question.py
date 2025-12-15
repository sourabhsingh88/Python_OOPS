# Create studetn class that takes name & marks of 3 subjects as argumen in cunstructor
# create method to print avg

class Student :
    school = "SAM"

    def __init__(self , name , marks):
        self.marks  = marks
        self.name = name

    def avg(self):
        sum = 0
        count = 0
        for i in self.marks :
            sum+= i
            count += 1
        print (f"hi {self.name} your total marks are {sum} of {count} subjects")
        avg = sum / count
        print(f"and your avg marks are {avg}")


s1 = Student( "sourabh",[15,12,45])
s1.avg()