#Python program to demonstrate multiplle inheritance    
class Mother:
    mothername=""
    def mother(self):
        print(self.mothername)
#Base class2
class Father:
    fathername=""
    def father(self):
        print(self.fathername)
#Derived class
class son(Mother,Father):
    def parents(self):
        print("Father :",self.fathername)
        print("Mother ",self.mothername)
#Driver's code
s1=son()
s1.fathername="abc"
s1.mothername="xyz"
s1.parents()                        