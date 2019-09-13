class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    
    def __init__(self, initx, inity):
        """ Create a new point at the given coordinates. """
        self.x = initx
        self.y = inity
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distancefromOrigine(self):
        return((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return  "x = " + str(self.x) + " y = " + str(self.y)

p = Point(2,4)

print(p)
    