#Python program to demonstrate multilevel inheritance
class Grandfather:
    def __init__(self,grandfathername):
        self.grandfathername=grandfathername
#Intermediate class
class Father(Grandfather):
    def __init__(self, grandfathername,fathername):
        self.fathername=fathername
        #invoking constructor of Grandfather class
        Grandfather.__init__(self,grandfathername)
#Derived class
class Son(Father):
    def __init__(self, grandfathername, fathername,sonname):
        self.sonname=sonname
        #invoking constructor of father class
        Father.__init__(self,fathername,grandfathername)
    def print_name(self):
        print('grandfather name',self.grandfathername)
        print("Father name",self.fathername) 
        print("Son name:",self.sonname)
#Driver code
s1=Son('Pushkar','Pushkar','push')
print(s1.grandfathername)
s1.print_name()           

