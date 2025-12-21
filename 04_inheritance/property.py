class Student:
    def __init__(self, phy , math , chem):
        self.phy = phy
        self.math = math
        self.chem = chem


    @property
    def percentage(self):
        total = self.phy  + self.math + self.chem
        print("Total : " , total)
        per = str(total / 3 ) + "%"
        print("Percantange are : " , per)


s1 =Student(15 , 15 , 15 )
s1.percentage
s1.phy = 20
s1.percentage