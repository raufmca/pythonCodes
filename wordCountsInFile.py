""" Uses a dictionary to count the number of occurrences of each
word in a text file. """


import sys # For sys.argv global command line arguments list

def main():
    """ Counts the words in a text file. """
    if len(sys.argv) < 2:
        print(' Usage of python word count <filename>')
        print(' where <filename> is the name of text file ')
    else:
        filename =  sys.argv[1]
        
        counters = {} # Initialize counting dictionary
        
        with open(filename , 'r') as f: # Open the file for reading
            content =  f.read() # Read in content of the entire file
            words = content.split()  # Make list of individual words
            
            for word in words:
                word = word.upper()
                
                if word not in counters:
                    counters[word] = 1
                else:
                    counters[word] += 1
            
            for word, count in counters.items():
                print(word, count , sep = '-' )


if __name__ == '__main__':
    main()
            
            
            
        
        