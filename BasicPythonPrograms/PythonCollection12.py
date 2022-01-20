#Python program to demonstrate userlist
from collections import UserList
#Creating a List where deletions is not allowed
class MyList(UserList):
    #Function to stop dletions from list
    def remove(self,s=None):
        raise RuntimeError("Deletion not allowed")
    #Function to stop pop from list
    def pop(self,s=None):
        raise RuntimeError("Deletion not allowed")
#Driver's code
L=MyList([1,2,3,4,5,6])
#Inserting to list
L.append(8)
print("After Insertion")
print(L)
#Deleting from list
L.remove()