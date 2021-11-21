def findDivisible(numberList):
    print("Given  list is ",numberList)
    print("Divisible by 5 in a list")
    for num in numberList:
        if(num%5==0):
            print(num)
numberList=[10,55,21,26,55]
findDivisible(numberList)            