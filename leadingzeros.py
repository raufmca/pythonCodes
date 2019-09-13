# leadingzeros

# Request input from the user

num = int ( input ( 'Enter the number between 0 - 9999 : ' ) )

if num < 0:
    num = 0
if num > 9999:
    num = 9999

print ( end=' [ ' )

# Extract and print thousands-place digit

digit = num // 1000 # extract 1000 place number 
print ( digit, end='')
num %= 1000

digit = num // 100 # extract 100 place number 
print ( digit, end='')
num %= 100

digit = num // 10 # extract 1000 place number 
print ( digit, end='')
num %= 10

print (num, end='')

print(' ] ')

