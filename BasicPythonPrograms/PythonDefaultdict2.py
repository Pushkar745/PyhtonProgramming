#Python program to demonstrate 
#Default_factory argument of
#Defaultdict
from collections import defaultdict
#Defining the dict and passing
#lambda as default_factory argument 
d=defaultdict(lambda:"Not Present")
d["a"]=1
d["b"]=2
print(d["a"])
print(d["b"])
print(d["c"])
