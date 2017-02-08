#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding='utf-8') as fn:
        for line in fn:
            print (line, end=''))
