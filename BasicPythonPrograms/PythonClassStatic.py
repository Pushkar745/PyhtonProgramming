# Python program to demonstrate use of class method and static method
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# a class method to create a Person Object by birth year

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
        # A Static method to check if a Person is adult or not

    @staticmethod
    def isAdult(age):
        return age > 26


person1 = Person('Pushkar', 26)
person2 = Person.fromBirthYear('Pushkar', 1994)
print(person1.age)
print(person2.age)
# Print the Result
print(Person.isAdult(25))
