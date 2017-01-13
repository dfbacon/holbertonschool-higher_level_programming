#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return(None)
    best_score = sorted(my_dict.keys())
    return(best_score[-1])
