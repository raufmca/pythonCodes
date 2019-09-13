#num1, num2 = map(int, input('Enter 2 numbers = ').split())

#print ( num1, num2 )

#i = 1

#for i in range(num1,num2):
    #if ( i%3 ==0 and i%5 == 0 ):
        #print('Fizz--Buzz')
    #else:
        #if( i%3 == 0 ):
            #print('Fizz')
        #else:
            #if ( i%5 == 0 ):
                #print('Buzz')
            #else:
                #print(i)
    

#L, R = map(int, input().split())
#while R >= L:
   #print (L)
   #L=L+1
   
numArray1 = list(map(int, input().split()))
numArray2 = list(map(int, input().split()))

sumArray = []
for i in range(0, len(numArray1)):
    sumArray.append(numArray1[i]+numArray2[i])

# Print the sumArray
for element in sumArray:
    print(element, end=" ")
    
print("")


    