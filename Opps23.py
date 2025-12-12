# PROGRAM 23: Multilevel Inheritance

class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor called.")

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)  # Call Person constructor
        self.emp_id = emp_id
        print("Employee constructor called.")

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)  # Call Employee constructor
        self.department = department
        print("Manager constructor called.")

    def display(self):
        print("\nManager Details:")
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Department:", self.department)


# Creating object of Manager
m = Manager("Arjun", 101, "IT")
m.display()
