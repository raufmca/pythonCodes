def funcSimilar(myStr):
    '''
    a function takes a two-word string and returns True if both words 
    begin with same letter
    
    '''
    
    myLst = myStr.split()
    
    return myLst[0][0] == myLst[1][0]
        