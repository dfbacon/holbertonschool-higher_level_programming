#!/usr/bin/python3
def simple_delete(my_dict, key=""):
    if my_dict is None:
        return(None):
    if key is None or key is "":
        return(None)
    elif key not in my_dict:
        return(None)
    del my_dict[key]
    return(my_dict)
