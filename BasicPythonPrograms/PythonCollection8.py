#Python code to demonstrate nametuple() and _make(),_asdict()
from collections import namedtuple
#Declaring Nametuple
Student=namedtuple('Student',['name','age','DOB'])
#Adding values
S=Student('Pushkar','28','789654123')
#Initializing iterable
li=['abc','20','123456']
#Initializing dict
di={'name':"Pushkarm",'age':26,'DOB':'28111994'}
#Using_Make() to return namedtuple()
print("The namedtuple instance using iterable is :")
print(Student._make(li))
#Using _asdict () to return an OrderdDict()
print("The OrderedDict instance using namedtuple is :")
print(S._asdict())