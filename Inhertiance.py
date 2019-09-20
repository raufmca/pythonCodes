class Animal():
    '''
    it is for to demonstrate the inheritance
    Animal is my Base class with 3 methods
    '''
    
    def __init__(self):
        print("Animal Created")
    
    def eat(self):
        print('Eating ')
    
    def who_am_i(self):
        print("I am an animal")
    
# Deriving a class 
# syntax : class <child_class_name> (<Base Class Name):

class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)   # Creating the init of base class
        print("Dog file Created")
    
    def eat(self):
        print( " Dog Eating ")
    
    def who_am_i(self):
        print(" This is dog")
        
    def bark(self,name):
        print( " {} is barking as woof!!".format(name))
        