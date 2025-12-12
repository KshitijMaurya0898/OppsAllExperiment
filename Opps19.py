# PROGRAM 19: Method Overriding (Shape → Circle)

import math

class Shape:
    def area(self):
        print("Area of shape is undefined.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Overriding area() method
    def area(self):
        return math.pi * self.radius * self.radius


# Creating object
c = Circle(5)

# Calling overridden method
print("Area of Circle:", c.area())
