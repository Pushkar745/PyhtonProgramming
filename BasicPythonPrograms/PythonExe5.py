def isFirst_And_Last_Same(numberList):
    print("Given number list",numberList)
    firstelement=numberList[0]
    lastelement=numberList[-1]
    if(firstelement==lastelement):
        return True
    else:
        return False
numberList=[10,23,30,40,10]
print("result is ",isFirst_And_Last_Same(numberList))            