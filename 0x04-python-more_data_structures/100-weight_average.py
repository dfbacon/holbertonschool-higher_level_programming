#!/usr/bin/python3
def weight_average(my_list=[]):
    avg = sum(i[0] * i[1] for i in my_list)
    avg /= sum(i[1] for i in my_list)
    return(avg)
