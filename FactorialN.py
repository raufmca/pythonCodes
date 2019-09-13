# factorial of number 

def fact(n):
    """
    Computes n!
    Returns the factorial of n.
    """
    
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

def main():
    """ Try out the factorial funcations """
    print( "  0! = ", fact(0))
    print( "  3! = ", fact(3))
    print( "  5! = ", fact(5))
    print( "  7! = ", fact(7))
    print( " 10! = ", fact(10))
    print( " 15! = ", fact(15))

main()
    
    