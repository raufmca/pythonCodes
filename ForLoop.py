#For Loop, 

sum=0

for i in range( 1, 100):
    sum+=i

print(' Sume is = ' , sum )

# powers of 10 ---------------------------------

for n in range(16):
    print("{0:3}  {1:17} ".format(n, 10**n))
    
# Letters in the word ---------------------

word = input(' Enter the word = ')

for char in word:
    print(char)

# Formatted characters --------------------------

for c in 'ABCDEFGHI':
    print ( '[',c,']', end='', sep='')

# Count vowels in the given word/text---------------------------------

word = input (' Enter the text or word = ' )
vCount = 0

for c in word:
    if c=='A' or c=='a' or c=='E' or c=='e' or c=='I' or c=='i' or \
     c=='O' or c=='o' or c=='U' or c=='u':
        vCount += 1
        print ( '[' , c , ']' , end='', sep='')
print ('\n Number of vowels in given text\word = ', vCount )

#-------------------

#printing *'s----------------------------------

height = int ( input ( ' Enter the height f the pyramid = ' ) )
row=0

for row in range(height):
#print white spaces 
    for count in range(height - row ):
        print(end=' ')
    
    #printing *'s 
    for count in range(2*row+1):
        print (end='*')
    
    print()

#______________________________

# Printing the tables

size = int ( input ( 'Enter the table size = ' ) )

for row in range(1, size+1):
     
    for column in range(1, size+1):
        print ( '{0:3} '.format(row*column), end=' ')
    
    print ()
    
