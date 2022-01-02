# Python code to illustrate working of try
def divide(x, y):
    try:
        # Floor Division :Gives only Fractional part as Answer
        result = x // y
        print("Yeah! your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")


# look at parameters and note the working of program
divide(8, 5)
