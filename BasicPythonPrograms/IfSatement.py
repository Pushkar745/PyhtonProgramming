a=88
b=211
c=211
if a> b:
    print("B is greater than a ")
elif a==b:
    print("b and c are equal")
else:
    print("b is greater than a")    
#The elif keyword is python way of saying "if the previous conditions were not true , then try this condition"        
if c >a: print("c is greater than a ") #short Hand If 
print("A") if a> b else print("B")
print("A") if a > b else print("=") if a==b else print("b") # This Technique Know as Ternary Operators or Conditional Expressions 
if b>a and c>a:
    print("both condition are true ")

# logical operator and is used to combine conditional statements 
if a > b or c > a:
    print("At least one of the conditions is true ")
#Nested if 
x=41
if x >10:
    print("Above ten")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20 ")        
if b==a:
    pass #PAss statement avoid to getting an error  
