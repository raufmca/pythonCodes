
class Dog():
    '''
    Dog class which has 4 attributes 
    species
    breed,
    name,
    spots 
    and method called bark()
    '''
    
    def __init__(self,mybreed,myname,spots):
        
        self.breed = mybreed
        self.name = myname
        self.spots = spots
    
    def bark(self,number=2):
        print("{} is barking as Woof! for {} times ".format(self.name,number))
