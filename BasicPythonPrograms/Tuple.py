thistuple=("apple","banana","cherry")
tuple1=(1,5,9,17,65,1)#Allow Duplicate values 
#Tuple items are ordered,unchangeable ,and allow duplicate values.
#collection which is un ordered and unchangeable
tuple2=(True,True,False)
print(thistuple)
print(len(thistuple))
for x in thistuple:
    print(type(x))

print(thistuple[2]) #Access Tuples
print((thistuple[-1]))#negative indexing
print(thistuple[1:3])#Range
print(thistuple[-3:-1])#Range of negative indexing
if 1 in tuple1:
    print("yes , there is number one in Tuple")
if "apple" in thistuple: #pass parameter as string 
    print("Apple found ")    
    


