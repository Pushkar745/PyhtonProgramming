# Python program to demonstrate finally
# No exeption Raised intry block
try:
    k = 5//0
    print(k)
# handeles zerodivision exeption
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    # This Block is always executed
    print('This is always executed')
