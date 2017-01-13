#!/usr/bin/python3
def complex_delete(my_dict, value):
    delete = []
    for i in my_dict.keys():
        if my_dict[i] == value:
            delete.append(i)
    for i in delete:
        del my_dict[i]
    return(my_dict)
