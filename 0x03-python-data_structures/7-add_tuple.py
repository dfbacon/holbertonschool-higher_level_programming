#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = []
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    if len(tuple_a) == 1:
        tuple_a = tuple_a[0], 0
    if len(tuple_b) == 1:
        tuple_b = tuple_b[0], 0
    i = tuple_a[0] + tuple_b[0]
    j = tuple_a[1] + tuple_b[1]
    new.append(i)
    new.append(j)
    return(new[0], new[1])
