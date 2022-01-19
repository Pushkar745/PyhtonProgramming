class MyClass: #its a class
    x=5*5 # class body 
p=MyClass() #p is object
print(p.x) #x is property name 
#Insert Function that print a greeting ,and execute it on the p1 obj
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is "+self.name)
        
p1=Person("Pushakr", 26)

p1.myfunc()

#The self papameter is a refernce to the current instance of the class,and is used to access variable that belong to the class

