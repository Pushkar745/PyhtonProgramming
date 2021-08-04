thislist=["apple","banana","cherry"]
i=0
while i < len(thislist):
    print(thislist[i])
    i=i+1
[print(x) for x in thislist]
#Looping Using List Comprehension    
mylist=thislist.copy()
mylist1=list(thislist)
print(mylist1)
print(mylist)