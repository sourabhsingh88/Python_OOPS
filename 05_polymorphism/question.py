class Circle:
    def __init__(self , radius):
        self.radis = radius

    def area(self):
        return (22/7) * self.radis**2

    def perimeter(self):
        return 2 *(22/7) * self.radis

c1 = Circle(5)
print(c1.area())
print(c1.perimeter())