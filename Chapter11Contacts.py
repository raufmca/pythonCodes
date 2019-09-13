contacts = {}

running = True 

while running:
    cmd = input ( 'A)dd  D)elete  L)ookup  Q)uit ' )
    
    if cmd == 'A' or cmd == 'a':
        name = input(' Enter the name of the person = ' )
        print( ' Enter the number of ' , name , end = ' ')
        num = int ( input () )
        contacts[name] = num
    
    elif cmd == 'D' or cmd == 'd':
        name = input ( ' Enter the person name which you want to delete = ' )
        del contacts[name]
    
    elif cmd == 'L' or cmd == 'l':
        name = input( ' Enter whose number you want to display = ' )
        print( name , contacts[name])
    
    elif cmd == 'Q' or cmd == 'q':
        running = False
    
    else: 
        print ( cmd , ' is not valid command ' )

