# PROGRAM 21: Multiple Inheritance

class Father:
    def father_message(self):
        print("Message from Father.")

class Mother:
    def mother_message(self):
        print("Message from Mother.")

class Child(Father, Mother):
    def child_message(self):
        print("Message from Child.")

# Creating object of Child
c = Child()

# Calling methods from both parents and child
c.father_message()
c.mother_message()
c.child_message()
