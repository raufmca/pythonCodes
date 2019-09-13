def readFile(filename):

    """ Read the comma-separated integer data from the text file
    named filename and return the data in a list. """
    
    result = [] 
    
    with open ( filename , 'r' ) as f:
        
        for line in f:
            
            result += [ int(x.strip()) for x in line.rstrip(", \n").split(',') ]
        
        return result

def main():
    
    lst = readFile(input('Enter the filename = '))
    print(lst)

if __name__ == '__main__':
    main()

    