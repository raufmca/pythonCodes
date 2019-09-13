def next_cnt():
    cnt=0
    cnt += 1 
    return cnt


global_cnt = 0
#global global_cnt

def next_cnt2():
    global global_cnt
    global_cnt += 1 
    return global_cnt

def main():
    for i in range(0,5):
        print(' Funcation First = ' , next_cnt() , ' Second Funcation = ' , next_cnt2())

if __name__ == '__main__':
    main()

#main()

#_______________________________

def sum(m=0, n=0, r=0):
    return m + n + r

def main():
    print('1', sum())
    print('2', sum(4))
    print('3', sum(4, 5))
    print('4', sum(5, 4))
    print('5', sum(1, 2, 3))
    print('6', sum(2.6, 1.0, 3))

main()
