# Program to depict else clause with try-except
# Function which return a/b
def AbyB(a, b):
    try:
        c = ((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)


# Driver Program to test above fuction
AbyB(4.2, 6.2)
AbyB(6.2, 4.2)
