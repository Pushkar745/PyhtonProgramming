# Program to depict else clause with try-except
# Function which return a/b
def AbyB(a, b):
    try:
        c = ((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b result in 0 ")
    else:
        print(c)


# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
# Initalize the amount variable
amount = 10000
# check that you are eligible to Purchase DSA Self paced or not
if(amount > 2999):
    print("You are eligible to purchase Dsa self Paced")
