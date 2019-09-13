
from math import sqrt 

def is_prime(n):
    """
    Determines the primality of a given value.
    n an integer to test for primality.
    Returns true if n is prime; otherwise, returns false.
    """    
    root = round(sqrt(n)+1)
    
    #find the prime number by dividing the number 
    
    for trail_factor in range ( 2, root):
        if n % trail_factor == 0:
            return False 
        return True
    
def main():
    """
    Tests for primality each integer from 2 up to a value provided by the user.
    If an integer is prime, it prints it; otherwise, the number is not printed.
    """
    
    max_val = int ( input ( ' Enter the number till where prime number has to display = ' ) )
    
    for val in range( 2, max_val+1 ):
        if is_prime(val):
            print(val, end = ' ')
    print()

main()
