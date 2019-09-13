def funcrev(s):
    '''
    Given a sentence, return a sentence with the words reversed
    'I am home' -> home am I'
    
    '''
    
    lst = s.split()
    
    lst.reverse()
    
    #revers_word = lst[::-1]
    
    return " ".join(lst)