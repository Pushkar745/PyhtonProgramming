#Python has two primitive loop commands
#while loops 
#for loops 
i = 1
while i< 6:
    print(i)
    i +=1 
    #note :remember to increment i,or else the loop will continue forever
# the break Statement
# with the break statement we can stop the loop even if the while condition is true 
i =2
while i<4:
    print(i)
    if i==3:
        break
    i +=1    
#continue Statement
i=0
while i<4:
    i+=1
    if i==3:
        continue
    print(i)
#else statement
i =1
while i<5:
    print(i)
    i+=1
else:
    print("i is no longer less than 5")    
