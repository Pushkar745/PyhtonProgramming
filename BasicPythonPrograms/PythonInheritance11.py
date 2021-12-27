#Python program to demonstrate Hierachical inheritance
class parent:
    def fun1(self):
        print("This is function is in parent class")
#Derived class1
class Child1(parent):
    def fun2(self):
        print("This function is in child 1")
#Derived class2
class Child2(parent):
    def fun3(self):
        print("This is function is in child 2")
#Driver's code
object1=Child1()
object2=Child2()
object1.fun1()
object1.fun2()
object2.fun1()
object2.fun3()        
