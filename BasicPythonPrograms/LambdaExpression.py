x=lambda a: a+10
print(x(45))
#lambda argu:expression 
y=lambda a,b :a*b
multi=y(8,5)
print(multi)
z=lambda a,b,c :a*b*c
multi1=z(87,5,2) #Summarize argument
print(multi1)
#The power of lambda is better shown when you use them as an anonymous function inside another fuction.
def myfunc(n):
    return lambda a: a*n
mydoubler=myfunc(2)
print(mydoubler(22))
#Use lambda functions when an anonymous fuction is required for a short period of time.
