
s = {8: 44, 'Alpha': 'up', True: 'right', 'Beta': 100, 3.4: True, False: 'wrong', 15: [1, 2, 3]}

d = {'Abdul': 11, 'Summi': 22, 'Alhaam': 33, 'Kupi': 44}

for k in d:
    print(k, sep= '-' , end = ' ')
print()

for v in d.values():
    print ( v, end = ' ')
    
print()

print('-------------------------------')

for k,v in d.items():
    print(v, k, sep = ' ')
print()
