thisdict={
    "brand": "Honda",
    "model":"Aura",
    "year":2021
}
for x in thisdict:
    print(x)
    print(thisdict[x])#print all values in the dictionary 
#values() method to return values of a dictionary
for x in thisdict.values():
    print(x)
for i in range(len(thisdict)):
    print([i])    
#keys() methods to return the keys of dictionary
for x in thisdict.keys():
    print(x)    
#Loop thorugh both keys and values ,by using items() Method 
for x,y in thisdict.items():
    print(x,y)   
mydict=thisdict.copy()
print(mydict)     