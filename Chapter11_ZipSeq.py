def gen(n):
    """ Generates the first n perfect squares, starting with zero:
    0, 1, 4, 9, 16,..., (n - 1)ˆ2. """
    
    for i in range(n):
        yield i**2
        

for p in zip([10,20,30,40], gen(int(input('Enter the positive number in (0 to 10)')))):
    print(p, end = ' ')
    

for p in zip([1,2,3,4,5,6],[6,5,4,3,2,1,0]):
    print(p, end=' ' )
    
for (x,y) in zip([1,2,3,4,5,6],[6,5,4,3,2,1,0]):
    print( (x,y) , ' ' , (x+y))

[x+y for(x,y)in zip([1,2,3,4,5,6,7],[1,2,3,4,5,6,7])]

