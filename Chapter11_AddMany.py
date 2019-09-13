def sum(*nums):
    """
    Finds sum any numbers
    
    """    
    s=0
    for num in nums:
        s += num
    return s 

##print('Sum of numbers = ' , sum(1,2,3))
##print('Sum of numbers = ' , sum(1,2,3,4,5,6))

def sum1(num1, num2, *extra):
    """
    Finds sum any numbers, parameters can vary from 0 to n 
    
    """      
    
    s = 0
    s = num1 + num2
    
    for n in extra:
        s += n
      #  print(n, end=' ')
    return s

