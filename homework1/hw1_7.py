from math import pi
class Circle():
    def __init__(self, r):
        self.radius = r
    def area(self):
        return self.radius*self.radius*pi
    def perimeter(self):
        return 2*self.radius*pi
Pizza = Circle(16)
print(Pizza.area())
print(Pizza.perimeter())