#Python code to Demostrate working of and_(),OR_(),invert()
import operator
a=1
b=0
#Biwise and
print("The bitwise and of a and b is :",end=" ")
print(operator.and_(a, b))
#Bitwise or
print("Then bitwise or of a and b is:",end="")
print(operator.or_(a, b))
#Bitewise xor()
print("The bitwise xor of a and b is :",end=" ")
print(operator.xor(a, b))
#using invert() to invert value
operator.invert(a)
#printing modified value 
print("The inverted value of a is :",end="")
print(operator.invert(a))
