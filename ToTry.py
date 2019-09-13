# To check / to try 

x = 10 
#print(x)

#if input("Print value (y/n)?") == 'y' and x > 10:
    #print(x)
#else:
    #print('**')

#if x > 5:
    #pass
    #print("****")
#else:
    #print( 'Nothing')
    
#--------------------

#value = int ( input ( ' Enter the number b/w 0- 100 : ' ) )
#if value >= 0 and value <= 100:
        #print( 'In Range !!!!' )
#else:
        #print ( ' -----  Out of range  ----- ')

#i = int ( input ( ' Enter the value of i : ' )) 
#j = int ( input ( ' Enter the value of j : ' )) 
#k = int ( input ( ' Enter the value of k : ' )) 

#if i < j:
    #if j < k:
        #i = j
    #else:
        #j = k
#else:
    #if j > k:
        #j = i
    #else: 
        #i = k 
#print ( ' i = ' , i , ' j = ' , j , ' k = ' , k )
        
#----------------------------------

#n = int(input())
#if n < 1000:
    #print('*', end='')
#if n < 100:
    #print('*', end='')
#if n < 10:
    #print('*', end='')
#if n < 1:
    #print('*', end='')
#print()

#---------------------------------------

n = int(input())
if n < 1000:
    print('*', end='')
elif n < 100:
    print('*', end='')
elif n < 10:
    print('*', end='')
elif n < 1:
    print('*', end='')
print()

#________________________________

def proc(x):
    return x+2

def main ():
    x = proc(5)
    print(x)
    y = proc(4)
    print(y)
    
main()

#____________________________________

def proc(x,y):
    return 2*x+y*y

def main():
    print(proc(5,4))

main()

#______________________________________

def proc(x):
    print ( ' in function proc = ' , 2*x*x )

def main():
    num = 10
    print(' in main function = ' , proc(num) )

main()


#---------------------

def sum_range(n, m=100):
    sum = 0
    for val in range ( n, m+1 ):
        sum += val
    return sum

print ( " Some of the given values = " , sum_range(1))

#---------------------

def sum_range(n, m):
    sum = 0
    for val in range ( n, m+1 ):
        sum += val
    return sum

print ( " Some of the given values = " , sum_range(1, 100))

#---------------------

def sum_range(n=1, m):
    sum = 0
    for val in range ( n, m+1 ):
        sum += val
    return sum

print ( " Some of the given values = " , sum_range(100))

#---------------------

def sum_range(n=1, m=100):
    sum = 0
    for val in range ( n, m+1 ):
        sum += val
    return sum

print ( " Some of the given values = " , sum_range())

#____________________-

def gen():
    yield 3
    yield 'wow'
    yield -2
    yield 25.34
    
print('-------')
print(gen)