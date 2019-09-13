def lesser_even_func(m,n):
    '''
    Function that returns the lesser of two given numbers if 
    both numbers are even, but returns the greater if one or both 
    numbers are odd
    '''
    if m%2 ==0 and n%2 == 0:
     #   if m < n :
     #       return m
     #   else: 
     #       return n
        return min(m,n)
    else:
        #if n > m :
        #    return n
        #else:
        #    return m
        return max(m,n)
    
    