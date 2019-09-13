class Point:
    
    def __init__(self, initx, inity):
        self.x = initx
        self.y = inity
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distOrigin(self):
        return ((self.x ** 2) + ( self.y ** 2) * 0.5 )
    
    def __str__(self):
        return "X = " + str(self.x) + " Y = " + str(self.y)
    
    def halfway(self, trgt):
        mx = ( self.x + trgt.x ) / 2
        my = ( self.y + trgt.y ) / 2 
        return Point(mx , my)
    
    def distFromPoint(self, trgt):
        return ( self.x ** trgt.x + self.y ** trgt.y )
    
    def reflect_x(self):
        return(self.x)


p = Point(3, 4)

q = Point(5, 12)

mid = p.halfway(q)

new = p.distFromPoint(q)

print( '***', mid )

print(mid)

print(mid.getX())
print(mid.getY())

print('----' , new )
               
print(p.reflect_x())

print('#########', p.distOrigin())

