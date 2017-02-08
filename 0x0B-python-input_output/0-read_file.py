#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as fn:
        fn_data = f.read()
    print ("{}".format(fn_data), end='')
