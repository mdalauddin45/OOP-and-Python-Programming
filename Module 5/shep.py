from math import *
class Shape:
    def __init__(self,name) -> None:
        self.name = name

class Reactangle(Shape):
    def __init__(self, name,l,w) -> None:
        self.l=l
        self.w=w
        super().__init__(name)
    def area(self):
        return self.l * self.w

class Circle(Shape):
    def __init__(self, name,radius) -> None:
        self.radius=radius
        super().__init__(name)
    def area(self):
        return pi * self.radius * self.radius