# PROGRAM 20: Polymorphism Example

class Bird:
    def fly(self):
        print("Some birds can fly.")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies high in the sky.")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly, it swims.")

# Function demonstrating polymorphism
def show_flying(bird):
    bird.fly()

# Creating objects
s = Sparrow()
p = Penguin()

# Calling function with different objects
show_flying(s)
show_flying(p)
