#_fields and _replace
import collections
Student = collections.namedtuple('Studnet', ['name', 'age', 'DOB'])
S = Student('Pushkar', '27', '20111994')
# Using _fields to display all the keynames of namedtuple()
print("All the fields of students are ")
print(S._fields)
# ._replace return a new namedtuple , it does not modifiy the original
print("return a new namedtuple")
print(S._replace(age='28'))
print(S)
