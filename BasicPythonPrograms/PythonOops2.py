#class For Dog
class Dog:
    #class Variable
    animal='Dog'
    # THe Init Method or constructor
    def __init__(self,breed,color):
        #Instant Variable
        self.breed=breed
        self.color=color
#Object of Dog class
Rodger=Dog("Pug","Brown")
Buzo=Dog("Bulldog","Black")
print('Rodger details:')
print('Rodger is a ',Rodger.animal)
print('Breed:',Rodger.breed)
print('Color',Rodger.color)
print('\nBuzo details:')
print('Buzo is a ',Buzo.animal)
print('Breed',Buzo.breed)
print('color',Buzo.color)
#class variable can be accessed using class
print("\nAccessing class variable using class name")
print(Dog.animal)        


