#Python program to demonstrate defaultdict
from collections import defaultdict
#Defining the dict
d=defaultdict(int)
L=[1,2,3,4,2,4,1,2]
#Iterate through the list
#For keeping the count 
for i in L:
    #The defalult value is 0
    #So there is no need to 
    #Enter the key first
    d[i]+=1
print(d)