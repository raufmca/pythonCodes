def func4(s):
    '''
    
    a function that capitalizes the first and fourth letters of a name
    ('macdonald') --> MacDonald

    '''
    if len(s) == 0:
        return False
    if len(s) >= 4:
        o = s[0].upper()
        f = s[3].upper()
        ns = o + s[1:3] + f + s[4:]
    else:
        o = s[0].upper()
        ns = o + s[1:]
    return ns

#one more logic 
    
    #first_half = s[:3]
    #second_half = s[3:]
    
    #retunr first_half.captalize()+second_half.capatalize()