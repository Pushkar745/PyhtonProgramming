# Program to handle multiple errors with one except statement
def fun(a):
    if a < 4:
        # throws ZeroDivisionError for a =3
        b = a/(a-3)
    # throw NameError id a >=4
    print("value of b = ", b)


try:
    fun(3)
    fun(5)
# Note that braces () are neccessary here for multiple exception
except ZeroDivisionError:
    print("ZeroDivisionError occurred and handled")
except NameError:
    print("NameError Occured and handled ")
