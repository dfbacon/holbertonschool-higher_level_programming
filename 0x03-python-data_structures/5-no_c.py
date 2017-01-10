#!/usr/bin/python3
def no_c(my_string):
    c = ['c', 'C']
    new_string = ''
    for i in my_string:
        if i not in c:
            new_string += i
    return (new_string)
