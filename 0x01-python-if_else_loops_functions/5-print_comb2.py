#!/usr/bin/python3
for i in range(0, 100):
    if (i < 10):
        print(0, i, sep='', end=', ')
    elif (i > 9 and i < 99):
        print(i, end=', ')
    else:
        print(i)
