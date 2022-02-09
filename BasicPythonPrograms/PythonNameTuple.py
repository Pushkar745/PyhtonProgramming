#_Make(),_asdict and "**" operator
import collections
Student=collections.namedtuple('Student',['name','age','DOB'])
S=Student('Pushka','27','28111994')
#init iterable
li=['Pushkarm','28','23121994']
#init dict
di={'name':"abc" ,'age':28,'DOB':'23121995'}
#using _make() to return nametuple()
print("The namedtuple instance using iterable is :")
print(Student._make(li))
#using _asdict() to return an OrderDict()
print("The OrderedDict instance using namedtuple is :")
print(S._asdict())
#using ** operator to return namedTuple from dict
print("The namedtuple instance from dict is :")
print(Student(**di))