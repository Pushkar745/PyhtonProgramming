def printEverIndexChar(str):
    for i in range(0,len(str)-1,-2):
        print("index[",i,"]",str[i])
inputStr="pynative"
print("Original Stirng ",inputStr) 
print("Printing only even index chars")
printEverIndexChar(inputStr)       