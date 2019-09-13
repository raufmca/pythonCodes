# Random functinos 

from random import randrange, seed

#seed(3)

#for i in range(0,100):
    #print(randrange(0,100), end = ' ')
#print()

#-----------------------------------------------------

# rOLL THE DIE 3 TIMES 

#from random import randomrange

for i in range(0, 3):
    #Generate random number in the range 1..7
    val = randrange(1, 7)
    
    #Show the die
    print('+----+')
    if val == 1:
        print("|    |")
        print("| *  |")
        print("|    |")
    elif val == 2:
        print("|*   |")
        print("|    |")
        print("|   *|")        
    elif val == 3:
        print("|*   |")
        print("|  * |")
        print("|   *|")         
    elif val == 4:
        print("|*  *|")
        print("|    |")
        print("|*  *|")         
    elif val == 5:
        print("|*  *|")
        print("|  * |")
        print("|*  *|")  
    elif val == 6:
        print("|*  *|")
        print("|*  *|")
        print("|*  *|")     
    else:
        print( ' *** Invalid Number ***' )
    print('+----+')        

#-------------------------------------------

from random import choice 

for i in range ( 10 ):
    print( choice (("one", "two", "three", "four", "five", "six", "seven", \
                   "eight", "nine", "ten" ) ) )
    

# ----------- Exit Program -------------

import sys 
sum = 0

while True:
    x = int ( input ( ' Enter the number (999 ends) = '))
    
    if x == 999:
        sys.exit(0)
    sum += x
    
    print ( ' Sum is = ', sum , end = ' ' )
    
#------------------------------------

x1 = eval ( input ( " Entery x1 ? " ) )
print(' x1 = ' , x1 , ' type: ' , type(x1) )

#------------------

while True:
    exec(input(">>>"))