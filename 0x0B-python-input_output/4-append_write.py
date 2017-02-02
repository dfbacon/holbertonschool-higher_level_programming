#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as fn:
        fn.seek(0, 2)
        return fn.write(text)
