# moreefficientprimes.py

from math import sqrt 

max_val = int ( input ( 'Enter the value till what number u want to display prime numbers = ' ) )
val = 2

while val <= max_val:
    #See if value is prime
    is_prime = True 
    trail_factor = 2
    root = sqrt(val)
 #   print(' root = ' , root )
    
    while trail_factor <= root:
        if val % trail_factor == 0:
            is_prime = False    # Found a factor
            break
        trail_factor += 1   # Try the next potential factor
    
    if is_prime:
        print( val, end = ' ' )
    val += 1 
print()

    