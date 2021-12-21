# A Python Program to demomstrate inheritance
class Base(Object):
    # construtctor
    def __init__(self, name):
        self.name = name
    # TO get name

    def getName(self):
        return self.name
# Inheritance or sub class(Note person in bracket)


class Child(Base):
    # constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

        # To get name
    def getAge(self):
        return self.age
# Inherited or sub class(Note person in bracket)


class GrandChild(Child):
    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age, address)
        self.address = address
        # To get address

    def getAddress(self):
        return self.address


# Driver code
g = GrandChild("Pushkar", 27, "India")
print(g.getAddress(), g.getName(), g.getAddress())
