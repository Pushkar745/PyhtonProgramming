thislist=["apple" , "banana","cherry"]
list1=[1,2,3,4,5,6,7]
list2=[True,True,False]
myList=list(("Pushkar","Manasi"))
print(thislist)
print(len(thislist))
print(thislist[0])
for x in thislist:
    print(x)
thislist.append("kiwi")    
print(thislist)
print(type(list1))
print(myList)
print(thislist[-1])
print(thislist[:2])
print(list1[1:6])
print(list1[-2:-5])
if 2 in list1:
    print("Yes this item exist in list1")
myList[1]="Love"    
print(myList)
thislist[1:2]=["blackcurrant","watermelon"]
print(thislist)
myList.insert(1, "Manasi")
print(myList)
list1.extend(list2)
print(list1)
list1.remove(3)
print(list1)
list1.pop(1)
print(list1)
thislist.pop()
print(thislist)
del thislist[0]
print(thislist)
del list2
list1.clear()
print(list1)