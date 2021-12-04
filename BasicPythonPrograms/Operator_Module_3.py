import operator
s1="Marlin"
s2="beard"
print("The Concatenated string is :",end="")
print(operator.concat(s1,s2))
#using contains() to check if s1 contains s2
if(operator.contains(s1, s2)):
    print("Marlin Contains Beard")
else:
    print("Marlin Does not contains Beard")
        