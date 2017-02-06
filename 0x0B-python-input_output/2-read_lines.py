#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as fn:
        if nb_lines <= 0:
            print(fn.read(), end='')
        else:
            for i in range(nb_lines):
                print(fn.readline(), end='')
