#from IPython.display import clear_output

#import os


def display_board(board):
    
    '''
    Step 1: Write a function that can print out a board. 
    Set up your board as a list, where each index 1-9 corresponds 
    with a number on a number pad, so you get a 3 by 3 board representation.
    
    '''

    
    print()
    
    #clear_ouput()
    
    print('  ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' | ')
    print('  ------------')
    print('  ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' | ')
    print('  ------------')
    print('  ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ')
    
    print()
    print('======================')
    print()
    
    
#test_board= ['  '] * 10 

test_board = ['#','X','O','X','O','X','O','X','O','X']

display_board(test_board)

def player_input():
    '''
    Ouput = ( Player 1 Marker , Player 2 Marker )
    
    '''
    
    marker = ' '
    
    while marker != 'X' and marker != 'O':
        marker = input (' Player 1 choose X or O = ').upper()
        
        if marker == 'X':
            return ( 'X' , 'O' )
        else:
            return ( 'O', 'X')

def place_marker(board, marker, position):
    '''
    Step 3: Write a function that takes in the board list object, 
    a marker ('X' or 'O'), and a desired position (number 1-9) 
    and assigns it to the board.
    
    '''
    board[position] = marker

place_marker(test_board, '#' , 4)
display_board(test_board)
              
def win_check():
    '''
    gStep 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
    '''