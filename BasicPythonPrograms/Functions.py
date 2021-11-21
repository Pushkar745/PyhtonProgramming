def my_function(fname):
    print(fname + " refsnes ")
    print("hello from a function")
my_function("Email")
my_function("Tobias")
my_function("Linus")
#arguments
def Myfunction(fname1,lname):
    print(fname1+" "+lname)
Myfunction("Emil", "Refsnes") 
def Arbitrary(*kids):
    print("The youngest child is "+kids[2])
Arbitrary("Emil","Tobias","Linus")  
def Arbitrary1(**kidsn):
    print("HIs last name is" +kidsn["lname2"])
Arbitrary1(fname="Tobias", lname2="Refsnes")
def DefaultParameters(country="Norway"):
    print("I am from "+country)
DefaultParameters("sweden")
DefaultParameters("Indian")
DefaultParameters()

def ReturnValues(x):
    return 8 * x
print(ReturnValues(3))
print(ReturnValues(5))
print(ReturnValues(4))    