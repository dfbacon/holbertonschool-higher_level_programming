#!/usr/bin/python3
def number_keys(my_dict):
    list(my_dict.keys())
    num = 0
    for i in range(len(my_dict)):
        num += 1
    return(num)
