# PROGRAM 14: Student Class

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)


# Creating objects
s1 = Student("Aman", 101, 85)
s2 = Student("Riya", 102, 92)

# Displaying student details
s1.display()
print()
s2.display()
