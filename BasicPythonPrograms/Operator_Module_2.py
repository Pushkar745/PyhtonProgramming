#Python code to demonstrate working of 
#setitem , delitemand getitem
import operator
#Initializing list
li=[1,5,6,7,8]
#printing orginal list
print("The original list is :",end="")
for i in range(0,len(li)):
    print(li[i],end=" ")
print("\r")
#using delitem() to delete value at 2nd index
operator.delitem(li, 1)
#operator.delitem(li, 5) listassinment index out of range 
#printing modified list after delitem
print("The Modified list after delitem() is :" ,end="")
for i in range(0,len(li)):
    print(li[i],end=" ")
print("\r")
#Using getitem() to access 4th element
print("The 4th element of list is :",end=" ")
print(operator.getitem(li, 3))
#print(operator.getitem(li, 4)) List index out of range
