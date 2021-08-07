set1={"a","b","c"}
set2={1,2,3}
print(set1.union(set2))
print(set1.intersection(set2))
set1.update(set2)
print(set1)
#note both Union()  and update() will exclude any duplicate
x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
x.intersection_update(y)
print(x)
#The Intersection () Method will return a new set, that only contains that are present in both sets
x.intersection(y)
print(x)
x.symmetric_difference_update(y)
#The symmetric_difference_update(y)method will keep only the elements that are NOT present in both sets
z=x.symmetric_difference(y) #will return a new set ,that contains only the element that are NOT present 
print(z)