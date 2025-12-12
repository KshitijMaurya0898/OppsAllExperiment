# PROGRAM 16: Abstract Class Shape

from abc import ABC, abstractmethod
import math

# Abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Subclass: Circle
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


# Subclass: Rectangle
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Testing the classes
c = Circle(5)
r = Rectangle(4, 6)

print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())

print("\nRectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())
