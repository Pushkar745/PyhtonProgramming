#Python code to demonstrate how parent constructors are called
class Person(object):
    #__init__is know as the constructor
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
#Child class
class Employee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        #invoking the __init__of the parent class
        Person.__init__(self, name, idnumber)
#creation of an object variable or an instance
a=Employee('Pushkar', 745,800000, 'AI Developer')
#calling a function of the calss person using its instance    
a.display()    
