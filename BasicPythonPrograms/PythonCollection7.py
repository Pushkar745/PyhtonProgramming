# Pyhton code to demonstrate nametuple()
from collections import namedtuple
# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])
# Adding Values
S = Student('Pushkar', '28', '123456789')
# Access using index
print("The Student age using index is :", end="")
print(S[1])
# Access using name
print("The Student name using keyname is :", end="")
print(S.name)
