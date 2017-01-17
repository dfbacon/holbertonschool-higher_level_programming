#!/usr/bin/python3
def add_integer(a, b):
    if isinstance( a, float ) or isinstance( b, float ) is True:
        a, b = int(a), int(b)
    if isinstance( a, int ) is False:
        raise TypeError("a must be an integer")
    if isinstance( b, int ) is False:
        raise TypeError("b must be an integer")
    return(a + b)
