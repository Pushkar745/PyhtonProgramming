#Python program to demonstrate userstring
from cgi import print_form
from collections import UserString
#Creating a Mutable String
class Mystring(UserString):
    #Function to append to string
    def append(self, s):
        self.data+=s
        #Function to remove from the string
        def remove(self,s):
            self.data =self.data.replace(s,"")
#Driver's code
s1=Mystring("Pushkar")
print("String after Appending:",s1.data)
#Appending to string
s1.append("m")
print("String After Appending:",s1.data)
#Removing from string
s1.remove("r")
print("String after Removing :",s1.data)