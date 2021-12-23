# A Python program to demonstrate inheritance
# Base class or Parent class
class child:
    # constructor
    def __init__(self, name):
        self.name = name
# To get name

    def getName(self):
        return self.name
# To check if this person is student

    def is_student(self):
        return False
# Derived class or child class


class Student(child):
    #True is returned
    def is_student(self):
        return True


# Driver code
# An Object of child
std = child("Pushkar")
print(std.getName(), std.is_student())
# An object of student
std = Student("Manasi")
print(std.getName(), std.is_student())
