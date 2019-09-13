#Opening file and writing data

f=open('data.dat', 'w')
f.write('\nFirstLine \n 2nd Line \n 3rd Line  \n 4th Line ')
f.close()

f = open('data.dat')
for line in f:
    print(line.strip())
f.close

