#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = dict(my_dict)
    for key, val in new_dict.items():
        new_dict[key] *= 2
    return(new_dict)
