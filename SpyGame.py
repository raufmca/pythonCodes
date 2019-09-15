def spyGame(nums):
    '''
    SPY GAME: Write a function that takes in a list of integers and returns True 
    if it contains 007 in order
    spy_game([1,2,4,0,0,7,5]) --> True
    spy_game([1,0,2,4,0,5,7]) --> True
    spy_game([1,7,2,0,4,5,0]) --> False
    '''
    
    code = [0,0,7,'x']
    
    # This code is using to check the 0,0,7
    # if we found first match that is 0 and then will pop out the 0 from code
    # and this code will become [0,7,'x']
    # if another 0 is present in list then pop it up and code becomes
    # [7,x] similary if 7 founds pop it up
    # when'x' remains in list then take siz of list and return 
    
    for num in nums:
        if num == code[0]:
            code.pop(0)
    
    return len(code) == 1 # only x remains and all other numbers found


    
    