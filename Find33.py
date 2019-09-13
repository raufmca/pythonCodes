def find33(num):
    '''
    Given a list of ints, return True if the array contains a 3 next 
    to a 3 somewhere.
    
    has_33([1, 3, 3]) -> True
    has_33([1, 3, 1, 3]) -> False
    has_33([3, 1, 3]) -> False
    
    '''
    
    #for i in range(0,len(num)-1):
        #if num[i] == 3 and num[i+1] == 3:
            #return True
    #return False
    
    for i in range(0,len(num)-1):
        if num[i:i+2] == [3,3]:
            return True
    return False
        
    
    
    
    