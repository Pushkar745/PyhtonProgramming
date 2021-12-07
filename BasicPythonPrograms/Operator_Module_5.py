#illustrate the difference between == and is operator
list1=[]
list2=[]
list3=list1
if(list1==list2):
    print("True")
else:
    print("False")
if(list1 is list2):
    print("True")
else:
    print("False") 
if(list1 is list3):
    print("True")
else:
    print("False")    
list3=list3+list2
if(list1 is list3):
    print("True")
else:
    print("False")
print(id(list1))
print(id(list2))    
            