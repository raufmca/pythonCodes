# Counts up from zero. The user continues the count by entering
# 'Y'. The user discontinues the count by entering 'N'.

#count = 0
#entry = 'Y'

#while entry != 'N' and entry != 'n':
    #print(count)
    #entry = input( ' Enter "Y" or to continue or "N" to quit ')
    
    #if entry == 'Y' or entry == 'y':
        #count += 1
    #elif entry != 'N' and entry != 'n':
        #print ( '"' + entry + '" is not valid choice')

        # Allow the user to enter a sequence of nonnegative
        # integers. The user ends the list with a negative
        # integer. At the end the sum of the nonnegative
        # numbers entered is displayed. The program prints
        # zero if the user provides no nonnegative numbers.

#entry = 0
#sum = 0

#print("Enter numbers to sum, negative number ends list:")

#while entry >= 0:
    #entry = int ( input () )
    #if entry > 0:
        #sum += entry 
#print ( " Sum of entered number is = " , sum )

#---------------------

n=1 

stop = int ( input ( ' Enter when to to stop ' ) )

while n <= stop:
    print(n)
    n += 1

print ('Done!')

#-----------------------------

height = int ( input (' Enter the hieght of the piramid = ' ) )
row = 0 # draw a raw for every unit of height 

while row < height:
    # Print leading spaces; as row gets bigger, the number of
    # leading spaces gets smaller
    count = 0
    while count < height - row:
        print (end='-')
        count +=1 
    
    count = 0
    
    # Print out stars, twice the current row plus one:
    # 1. number of stars on left side of tree
    # = current row value
    # 2. exactly one star in the center of tree
    # 3. number of stars on right side of tree
    # = current row value
    
    while count < 2*row + 1:
        print(end='*')
        count += 1 
    print()
    
    row += 1     
    
#----------------------------------------------------------------------------------