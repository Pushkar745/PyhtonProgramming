def sumNum(num):
    priviousNum=0
    for i in range(num):
        sum=priviousNum+i
        print("Current Number is ",i,"Previous Number",priviousNum,"sum",sum)
        priviousNum=i
print("Printing current and previous number sum in a given range(10)") 
sumNum(10
)       
