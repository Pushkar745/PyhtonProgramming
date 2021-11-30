#Check Plindrome NUmber
def palindrome(number):
    print("original number ",number)
    original_num=number
    reeverse_num=0
    while number>0:
        reminder=number % 10
        reeverse_num =(reeverse_num * 10) +reminder
        number = number // 10 # Floor division 
        #check number
        if original_num == reeverse_num:
            print("given number is palidrome")
        else:
            print("The given number is not palidrom ")
palindrome(252)
palindrome(123)  
print("original number", number)
original_num=number
