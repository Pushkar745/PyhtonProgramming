thistuple=("apple","banana","cherry")
#tuples are unchangeableBut there is workaround ,You can convert the tuple into alist
thistuple1=(1,5,1,5)
y=list(thistuple)
y[1]="kiwi"
y.append("orange")
y.remove("cherry")
del thistuple1
thistuple=tuple(y)
print(thistuple) 
print(type(thistuple))
