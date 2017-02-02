#!/usr/bin/python3
import json
import sys
import os.path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
argv = sys.argv
my_file = 'add_item.json'

try:
    fn = open(my_file)
    fn.close()
except:
    fn = open(my_file, 'w+')
    fn.close()

with open(my_file, "r+") as fn:
    if os.path.isfile(my_file):
        temp = load_from_json_file(my_file)
    else:
        temp = []
    count = 0
    for i in argv:
        if count != 0:
            temp.append(argv[i])
        count += 1
    save_to_json_file(temp, my_file)
