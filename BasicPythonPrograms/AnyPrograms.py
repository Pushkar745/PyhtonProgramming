list1=[]
list2=[]
for i in range(1,11):
    list1.append(4*i)
   #print(list1) print loopwise 
#print(list1) print 4 table

for i in range(0,10):
    list2.append(list1[1]%5==0)
print('See whether at least one number is divisible by 5 in list 1=>')
print(any(list2))
print(list1) 
print(list2)   
