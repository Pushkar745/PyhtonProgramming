#Instance variable inside methods 
#class for dog
class Dog:
    #class Variable
    animal='dog'
    def __init__(self,breed):
        #Instance variable
        self.breed=breed
        #add an instance variable
    def setcolor(self,color):
        self.color = color
        #Retrive instance variable
    def getColor(self):
        return self.color
Rodger=Dog("Pug") 
Rodger.setcolor("Brown")
print(Rodger.getColor())    