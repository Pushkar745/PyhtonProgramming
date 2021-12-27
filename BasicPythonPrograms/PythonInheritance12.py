#Python program to demonstrate hybrid inheritance
class School:
    def fun1(self):
        print("This is function is in school")
class Student1(School):
    def func2(self):
        print("This is function is in student 1")
class Student2(School):
    def fun3(self):
        print("This function  is in student 2")
class Student3(Student1,School):
    def fun4(self):
        print("This function is in student 3")
# Driver's code 
object=Student3()
object.fun1()
object.func2()