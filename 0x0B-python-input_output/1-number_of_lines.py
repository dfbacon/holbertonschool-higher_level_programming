#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, encoding='utf-8') as fn:
        i = 0
        for line in fn:
            i += 1
        return i
