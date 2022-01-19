#Python program to demonstrate userdict
from collections import UserDict
#Creating a Dictionary where deletion is not allowed
class MyDict(UserDict):
    #function to stop deletion from dict
    def __del__(self):
        raise RuntimeError("Deletion not allowed")
        #Function to stop pop from dict
    def poop(self,s=None):
        raise RuntimeError("Deletion not allowed")
        #Function to stop popitem from dict
    def popitem(self,s=None):
        raise RuntimeError("Deletion not allowed")
#Driver's code
d=MyDict({'a':1,'b':2,'c':3})
d.pop(1)


