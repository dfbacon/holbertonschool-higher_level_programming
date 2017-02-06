#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, mode='w', encoding='UTF-8') as fn:
        return fn.write(text)
