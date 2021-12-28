# Python Program to demonstrate private member
# Creating a derived class
class Base:
    def __init__(self):
        self.a = "Push"
        self.__c = "Pushkar"
# Creating a derived class


class Derived(Base):
    # Calling constructor of base class
    Base.__init__(self)
    print("calling private mmember of base class:")
    print(self.__c)


# Driver code
obj1 = Base()
print(Obj1.a)
