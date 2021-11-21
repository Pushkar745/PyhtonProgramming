class Person:
    def __init__(self,fname,lname): 
        self.firstname=fname  #proerties
        self.lastname=lname
    def printname(self): #Method
        print(self.firstname,self.lastname)
class Student(Person):  #child class
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        super().__init__(fname,lname)
    
#Use the person class to create an object,and then execute the printname method        
x=Person("Pushkar", "Baviskar") #X is an object of class Person
x1=Student("Manasi", "Pushkar") 
x.printname()  #call the printname method using object
#created a Parent class
x1.printname()
f=open("E:\Github profile\PythonProgramming\BasicPythonPrograms\Pushkar.txt","r")
print(f.read()) 
print(f.readline())
f.close() 
