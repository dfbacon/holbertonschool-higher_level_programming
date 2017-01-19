#!/usr/bin/python3
'''
This is the "add_integer" module.

The add_integer module supplies one function, add_integer(a, b).

For example:
>>> add_integer(1, 3)
4
'''

def add_integer(a, b):
    '''Return the sum of a and b, an exact integer.
    '''

    if isinstance( a, float ) or isinstance( b, float ) is True:
        a, b = int(a), int(b)
    if isinstance( a, int ) is False:
        raise TypeError("a must be an integer")
    if isinstance( b, int ) is False:
        raise TypeError("b must be an integer")
    return(a + b)
