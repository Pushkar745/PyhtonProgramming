# Demonstration A Class
class Dog:
    #A simple class attribute
    attr1= "mammal"
    attr2="Dog"
    # A sample method
    def fun(self):
        print("I am a ",self.attr1)
        print("I ma a ",self.attr2)
#Driver code
# Object instantiation        
Rodger =Dog()
print(Rodger.attr1)
Rodger.fun() 
