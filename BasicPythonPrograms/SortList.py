thislist=[100,50,65,82,23]
print(thislist[1])
thislist.sort()
print(thislist)
thislist.sort(reverse=True)
print(thislist)

def myfunc(n):
    return abs(n-50)
list1=[100,50,65,82,23]
list1.sort(key=myfunc)
print(list1)    
#Customize sort function