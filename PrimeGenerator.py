from math import sqrt

def is_prime(n):
    
    """ Returns True if nonnegative integer n is prime;
    otherwise, returns false """
    
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    
    trail_factor = 3
    
    root = sqrt(n)
    
    while trail_factor <= root:
        if n % trail_factor == 0:
            return False
        trail_factor += 2 
    
    return True

def prime_sequence(begin, end):
    """ Generates the sequence of prime numbers between begin and end. """
    
    for val in range(begin+1, end):
        if is_prime(val):
            yield val

def main():
    """ Make a list from a generator """
    primes = list ( prime_sequence( int(input ( 'enter the begin value = ' )) , int(input ('Enter the end value = ' ) ) ))
    
    print (primes)


if __name__ == '__main__':
    main()
    
    