def count(nums):
    neg_count , pos_count = 0, 0 
    
    for num in nums:
        if num < 0:
            neg_count += 1 
        else:
            pos_count += 1
    
    return neg_count, pos_count


def main():
    print('####')
    nums =  1 , -2 ,3 ,-4 ,5 , -6 , 7, 8 , -9 , 10

    print(count(nums))

#main()

if __name__ == '__main__':
    print('@@@@')
    main()