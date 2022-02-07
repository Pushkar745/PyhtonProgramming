#Python code to demonstrate namedtuple 
from collections import namedtuple
#Declaring nmaedTuple
Student= namedtuple('Student',['name','age','DOB'])
#Adding value
S=Student('Pushkar','27','28111994')
#Access using index
print("The Student age using index is:",end="")
print(S[1])
#Access using name
print("The Student name using keyname is :",end="")
print(S.name)