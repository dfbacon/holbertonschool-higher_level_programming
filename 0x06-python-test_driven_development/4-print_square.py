#!/usr/bin/python3
'''
This is the "print_square" module.

The print_square module supplies  one function.
print_square(size).

'''


def print_square(size):
    '''Print a square of # characters of size size.

    size: the length of one side of the square

    The argument must be of type int
    '''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
