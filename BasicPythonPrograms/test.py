import sys
a=10
b=10 
print(id(a))
print(id(b))
c=20
d=20
e=20
print(id(c))
print(id(d))
print(id(e))
print(sys.getrefcount(a))
print(sys.getrefcount(c))