#regularGenerator 

count = 0

def genrate_mult(m, n):
    global count
    while count < n:
        yield m * count 
        count += 1

def main():
    for mult in genrate_mult(3, 6):
        print( mult , end = ' ')
    print()

if __name__ == '__main__':
    main()
    