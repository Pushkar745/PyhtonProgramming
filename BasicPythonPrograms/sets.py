myset={"apple","banana","cherry"}
tropical= {"pineapple","mango","papaya"}
print(myset)
#Unorderd ,unchangelable and do not allow duplicate values
#  Once a set is created, you cannot change its items , but you can add new items 
print(len(myset))
print(type(myset))
#Important set() construtor 
thisset1=set((1,2,7,5,6,8)) #note the double round-brackets 
print(thisset1)
for x in thisset1:
    print(x)
print("banana" in myset)    
#Once a set is created , you cannot change its items , but you can add new items 
#to add one item to a set use the add() Method
myset.add("kiwi")
print(myset)
myset.update(tropical)
print(myset)
#update() method does not have to be a set, it can be any iterable object(tuples,list,dictionariesetc)
thislist=[1,15,2,6,53,5]
myset.update(thislist)
print(myset)
myset.remove("cherry")
#If the item to remove does not exit ,remove() will raise an error
thisset1.discard(9)
print(myset)
print(thisset1)
x= thisset1.pop()
print(x)
del thislist
