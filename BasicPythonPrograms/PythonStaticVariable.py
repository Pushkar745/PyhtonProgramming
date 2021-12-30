# Python Program to show that the variable with a value
# Assigned in class declaration,are class variables
# Class for computer Science student
class CSSStudent:
    stream = 'cse'

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


# Object of Css Student class
a = CSSStudent('Geek', 1)
b = CSSStudent('Nerd', 2)
print(a.stream)
print(b.stream)
print(a.name)
print(b.name)
print(a.roll)
print(b.roll)
# Class Variable can be accessed using class
# name also
print(CSSStudent.stream)  # print "cse"
# NOw if we change the stream for just a it won't be changed for b
a.stream = 'ece'
print(a.stream)
print(b.stream)
# To change the stream for all instance of the the class we can change it
CSSStudent.stream = "IT"
print(a.stream)
print(b.stream)
