#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list is []:
        return(0)
    avg = sum(i[0] * i[1] for i in my_list)
    avg /= sum(i[1] for i in my_list)
    return(avg)
