#!/usr/bin/python3
'''
This is the "say_my_name" module.

The say_my_name module supplies one function,
say_my_name(first_name, last_name="").

'''


def say_my_name(first_name, last_name=""):
    '''Print the string "My name is" followed by the arguments strings
    first_name: first name being passed
    last_name: last name being passed

    Both arguments must be of string type
    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print('My name is {} {}'.format(first_name, last_name))
