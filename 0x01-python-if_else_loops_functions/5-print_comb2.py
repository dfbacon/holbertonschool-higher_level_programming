#!/usr/bin/python3
for i in range(0, 100):
    if (i < 10):
        print('0{:d}'.format(i), sep='', end=', ')
    elif (i > 9 and i < 99):
        print('{:d}'.format(i), end=', ')
    else:
        print('{:d}'.format(i))
