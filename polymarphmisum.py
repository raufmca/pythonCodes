class Dog():
    '''
    Polymarphisum examples 
    '''
    
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return self.name + " says woof!"

class Cat():
    
    def __init__(self,name):
        self.name = name 
    
    def speak(self):
        return self.name + " says meow"
    