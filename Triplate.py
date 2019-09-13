def triplet(text):
    '''
    PAPER DOLL: Given a string, return a string where for every character in 
    the original there are three characters
    
    'Hello' -> HHHeeellllllooo
    
    '''
    res = ''
    for c in text:
        res += c*3
    
    return res