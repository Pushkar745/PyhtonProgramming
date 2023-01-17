import collections
from itertools import chain
dic1={'a':1,'b':2}
dic2={'b':3,'c':4}
dic3={'f':5}
#Init ChainMap
chain=collections.ChainMap(dic1,dic2)
#Printing chainMap using map
print("All the Chain Map Contents are :")
print(chain.maps)
#printing chainMap using map
print("Displaying new ChainMap:")
print(chain.maps)
#Displaying value associated with b before reversing
print("Value associated with b before reversing is :",end="")
print(chain['b'])
#reversing the ChainMap
chain.maps=reversed(chain.maps)
#Displaying value associated with b after reversing
print(chain['b'])