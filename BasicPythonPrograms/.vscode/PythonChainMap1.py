#Python code to demonstrate ChainMap    
#Init Dict
import collections
from ipaddress import collapse_addresses
from itertools import chain


dic1={'a':1,'b':2}
dic2={'b':3,'c':4}
#Init Chainmap
chain=collections.ChainMap(dic1,dic2)
#Printing Chinmap using maps
print("All The ChainMap contents are :")
print(chain.maps)
#Printing keys using keys()
print(list(chain.keys()))
#printing keys using keys()
print("All values of ChainMap are :")
print(list(chain.values()))
