#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = sorted(set(my_list))
    total = 0
    for i in range(len(my_list)):
        total += my_list[i]
    return(total)
