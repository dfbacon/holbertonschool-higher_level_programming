#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, 'a', 'UTF-8') as fn:
        return fn.write(text)
