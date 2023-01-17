#Access by name ,index and getattr
import collections
#Declaring nametuple
Student=collections.namedtuple('Student',['name','age','DOB'])
S=Student('Pushkar','27','28111994')
#Access using index
print("The Student age using index is :",end="")
#Access using name
print("The student name using keyname is:",end="")
print(S.name)
#Access using getattr
print("The Student DOB using getattr() is :",end="")
print(getattr(S,'DOB'))