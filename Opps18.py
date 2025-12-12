# PROGRAM 18: Extend Parent Method Using super()

class Animal:
    def sound(self):
        print("Animals make different sounds.")

class Dog(Animal):
    def sound(self):
        super().sound()     # Call parent class method
        print("Dog barks: Woof Woof!")

# Creating object
d = Dog()
d.sound()
