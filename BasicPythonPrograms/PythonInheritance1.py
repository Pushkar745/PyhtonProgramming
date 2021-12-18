#A python program to demonstrate inhertance
class Person(object):
    #constructor
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    #To Check if this person is an emloyee
    def isEmployee(self):
        return False
#Inheriated or subclass (Note person in bracket)
class Employee(Person):
    def isEmployee(self):
        return True
#Driver code
emp=Person("Pushkar") #An Object of person
print(emp.getName(),emp.isEmployee())
emp=Employee("Push")              
print(emp.getName(),emp.isEmployee())
