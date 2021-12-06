import operator
a=5
b=2
c=6
d=6
e=4
f=3
print(operator)
print(operator.add(a,b))
print(operator.sub(a,b))
print(operator.mul(a, b))
print("The true Division number is :",end=" ")
print(operator.truediv(a, b))
print("The Floor dividion is :",end="")
print(operator.floordiv(a, b))
print("The exponetiation of number is :",end="")
print(operator.pow(a, b))
print("The modulus of number is :",end= " ")
print(operator.mod(a, b))
if(operator.lt(c, d)):
    print("3 is less then e")
else:print("3 is not less then3")
if(operator.le(c, d)):
    print("3 is less than or equal to 3")
else:print("3 is not less than or equal to 3")
if(operator.eq(c, d)):
    print("3 is equal to 3")
else:print("3 is not equal to 3") 
if(operator.gt(e, f)):
    print("4 is greater than 3")
else:print("4 is not greater than  3")
if(operator.ge(e, f)):
    print("4 is greater than or equal to 3")
else:print("4 is not equal to or equal to 3")
if(operator.ne(e, f)):
    print("4 is not equal to 3")
else:print("4 is equal to 3")
