# Create a Circle class and initialize it with radius.
# Make two methods getArea and getCircumference inside this class.

import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return f"A circle with a radius of {self.radius}."

    def getArea(self):
        return math.pi * self.radius**2

    def getCircumference(self):
        return 2 * math.pi * self.radius


c1 = Circle(10)
print(c1.getArea())
print(c1.getCircumference())
print(c1)