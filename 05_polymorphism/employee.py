class Employee :
    def __init__(self , role , dept , salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print(f"Role : {self.role } ")
        print(f"Department : {self.dept} ")
        print(f"Salary : {self.salary}" )

class Engineer(Employee) :
    def __init__(self , name , age):
        self.name = name
        self.age = age
        super().__init__("Engineer" , "IT" , 15000)

e1 = Employee("Guard" , "Security" , 1500)
e1.showDetails()

eng1 = Engineer("Sawan" , 15)
eng1.showDetails()