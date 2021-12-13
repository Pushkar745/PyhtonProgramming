class Person:
    def __init__(self,name):
        self.name = name
        #Sample Method
        def say(self):
            print('Hello ,My name is ',self.name)
p=Person('Pushkar')
p.say()            