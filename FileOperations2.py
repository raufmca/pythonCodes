
"""
Uses Python's file class to store data to and retrieve data from
a text file.
"""
def read_data(filename):
    """ Print the elements stored in the text file named filename. """
    with open(filename) as f:
        for line in f:
            print(int(line) , end = ' ')

def write_data(filename):
    """ Allows the user to store data to the text file named filename. """
    with open(filename, 'w') as f:
        number = 0
        while number != 999:
            number = int ( input ( ' Enter the number = ' ))
            if number != 999:
                f.write(str(number)+'\n')
            else:
                break

def main():
    """ Interactive function that allows the user to
    create or consume files of numbers. """
    stop = False
    
    while not stop:
        cmd = input (' W)rite , \n R)ead , \n Q)uit = ' )
        if cmd == 'W' or cmd == 'w':
            write_data(input ('Enter the filename = ' ))
        elif cmd == 'R' or cmd == 'r':
            read_data(input ('Enter the filename = ' ))
        elif cmd == 'Q' or cmd == 'q':
            stop = True

main()
            
    
                