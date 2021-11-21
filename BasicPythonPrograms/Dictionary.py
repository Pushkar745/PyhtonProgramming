#used to store data values in key :value pairs 



thisdict={
    "brand": "Honda",
    "model":"Aura",
    "year":2021
}
print(thisdict)
print(thisdict["brand"])
print(type(thisdict))
x=thisdict.get("brand") #same result like print(thisdict["brand"]) 
x=thisdict.keys()
thisdict["color"]="blackshine"
#Get Values
x=thisdict.values() #The Values() method will return a list of all the values in the dictionary 
print(x)
thisdict["year"]=2020 #add items 
print(x)
thisdict.update({"year":"2021"})
print(thisdict)
#removing items
thisdict.pop("brand")
print(thisdict)
#The popitem() method removes the last inserted item 
thisdict.popitem()
print(thisdict)
del thisdict["model"]
print(thisdict)
#the clear() method empties the dictionary 
thisdict.clear()
print(thisdict)