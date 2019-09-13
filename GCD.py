##gcd program 

#num1 = int ( input ( ' Enter the number 1 = ' ) )

#num2 = int ( input ( ' Enter the number 2 = ' ) )

#min = num1 if num1 < num2 else num2  # to find smaller number 

#larg = 1 

#for i in range ( 1, min+1 ):
    #if num1 % i == 0 and num2 % i == 0:
        #larg = i
## print GCD

#print ( ' GCD of  ', num1 , ' and ' , num2 , ' = ' , larg )

#________________________

# Same funcation using funcations 

def GCD(num1, num2):
    min = num1 if num1 < num2 else num2 
    lar = 1 
    for i in range ( 1, min + 1 ):
        if num1%i == 0 and num2%i == 0:
            lar = i
    return lar 


num1 = int ( input ( ' Enter the number 1 = ' ) )

num2 = int ( input ( ' Enter the number 2 = ' ) )

print ( ' GCD of  ', num1 , ' and ' , num2 , ' = ' , GCD(num1,num2))