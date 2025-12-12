# PROGRAM 12: Implementation of Classes & Objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating objects
p1 = Person("Rahul", 20)
p2 = Person("Priya", 19)

# Displaying details
p1.display()
p2.display()
