# Count to ten and print each number with 0 parameter

def count_to_ten():
    for i in range(1,11):
        print(i, end=' ')
    print()

print ( ' Countdown starts now !!! ' )
count_to_ten()

print ( ' Countdown starts again  !!! ' )
count_to_ten()

#---------------------------------------

# Count print each number with 1 parameter

def countTo(n):
    for j in range(1,n+1):
        print(j, end=' ')
    print()

n = int ( input ( ' Enter the number for count = ' ) )
countTo(n)

#---------------------

def countTon(n):
    for i in range(1,n+1):
        print(i, end = ' ')
    print()
    

for j in range ( 1, 10 ):
    countTon(j)

#----------------------------------

def proc(x):
    return x**2

def proc(n):
    return n*2

def main():
    y = proc(5)
    print('--------' , y)

main()
