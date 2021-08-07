thistuple=("apple","banana","cherry")
tuple1=(1,5,8,2)
for x in thistuple:
    print(x)
for i in range(len(thistuple)):
    print([i])
    print(thistuple[i])
while i < len(thistuple):
    print(thistuple[i])
    i=i+1
tuple2=thistuple+tuple1
mytuple=tuple1 * 2
print(mytuple)
print(tuple2)    