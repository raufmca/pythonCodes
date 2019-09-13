class Fraction:
    
    def __init__(self, num, den):
        
        self.num = num
        self.den = den
        
    def __str__(self):
        
        return str(self.num) + "/" + str(self.den)
    
    def getNum(self):
        return self.num 
    
    def getDen(self):
        return self.den
    

myfrac = Fraction(10, 2)

print( myfrac )

print(myfrac.getNum())
print(myfrac.getDen())

