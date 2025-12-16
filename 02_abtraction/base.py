from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    # As every shape have its own dimension there fore
    # we are create init in child class if all have smae use abstrat class only
    def __init__(self, length, breadth):
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


r = Rectangle(10, 5)
print("Area:", r.area())
