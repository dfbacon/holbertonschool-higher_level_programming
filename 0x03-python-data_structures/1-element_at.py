#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > len(my_list) - 1 or idx <= -len(my_list) - 1:
        return (None)
    if my_list == None:
        return (None)
    return (my_list[idx])
