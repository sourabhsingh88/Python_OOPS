class Person :
    name  ="Sourab"

    def print_name(self):
        print(self.name)
    def change_name(self , name):
        # Person.name = name
        self.__class__.name = name

    #Or************************OR*****
    def change_name(self , name):
        # Person.name = name
        self.__class__.name = name

    @classmethod
    def chng_name(cls , name):
        cls.name = name
        print(cls.name)

p1 = Person()
p1.change_name("Singh")
p1.print_name() # Changes singh
print(p1.name)  # Changes singh
print(Person.name)  # Changes shing
p1.chng_name("khuman")
print(p1.name)  # Changes khuman

  
# CLASS METHODS = CLS
# STATIC METHODS = STAIC
# INSTANCE (NORMALE) METHOD  = SELF
