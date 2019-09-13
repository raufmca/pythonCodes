from random import randrange 

def func1(n):
    result = 0
    while n:
        result += n
        n -= 1
    return result

def func2(stars):
    for i in range(stars+1):
        print(end='*')
    print()

def func3(x,y):
    return 2*x*x + 3*y

def func4(n):
    return 10 <= n <= 20

def func5(a,b,c):
    return a <= b if b <= c else False

def func6():
    return randrange(0,2)


print(func1(5))

# print(func1()) # builtins.TypeError: func1() missing 1 required positional argument: 'n'

# print(func1(5, 2)) -- builtins.TypeError: func1() takes 1 positional argument but 2 were given

print(func2(5))
func2(5)
func2(0)
func2(-2)

print(func3(5, 2))

print(func3(5.0, 2.0))

#print(func3('A', 'B')) -- builtins.TypeError: can't multiply sequence by non-int of type 'str'

#print(func3(5.0)) -- builtins.TypeError: func3() missing 1 required positional argument: 'y'


print(func4(25))

print(func5(2, 4, 6))

print(func5(4, 2, 6))

if func5(2, 2, 6):
    print("Yes")
else:
    print("No")

print(func3(func1(3), 3))

print(func6(func6()))