#Python Program to demonstrate single inheritance
#Base class
class Parent:
    def fun1(self):
        print("This is function is in parent class")
#Derived class
class Child(Parent):
    def fun2(self):
        print("This function is in child class")
#Driver's code
object=Child()
object.fun1()
object.fun2()        