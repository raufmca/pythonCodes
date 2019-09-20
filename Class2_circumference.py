class Circle ():
    '''
    Calculates the circumference of a circle 
    
    Input radius 
    '''
    
    pi = 3.14
    
    def __init__(self,rad=1):
        self.rad = rad
    
    def calculate(self):
        
        return self.rad * self.pi * 2
    