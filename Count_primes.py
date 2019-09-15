def count_primes(num):
    '''
    COUNT PRIMES: Write a function that returns the number of prime numbers 
    that exist up to and including a given number
    
    '''
    
    if num <= 2:
        return False
    
    prime =  [0,1,2]
    
    x = 3
    
    while x <= num:
        
        for y in range(3,x,2):
            if x%y == 0:
                x += 2 
                break
        else:
            prime.append(x)
            x += 2
    print(prime)
    
    return len(prime)
            
            
    