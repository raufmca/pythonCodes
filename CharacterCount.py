string = input('Enter your string = ')

string = string.lower()

alphabate = 'abcdefghijklmnopqrstuvwxyz'

lt_ct = {}

for char in string:
    if char in alphabate:
        if char in lt_ct:
            lt_ct[char] = lt_ct[char] + 1
        else:
            lt_ct[char] = 1

keys = lt_ct.keys()

for char in sorted(keys):
    print(char, lt_ct[char])

