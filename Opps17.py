# PROGRAM 17: Method Overriding using super()

class Person:
    def info(self):
        print("I am a Person.")

class Student(Person):
    def info(self):
        super().info()   # Calling parent class method
        print("I am also a Student.")

# Creating object
s = Student()
s.info()
