#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for key, val in sorted(my_dict.items()):
        print('{} : {}'.format(key, val))
