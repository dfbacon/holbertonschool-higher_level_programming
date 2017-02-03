#!/usr/bin/python3
import json
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
argv = sys.argv

try:
    fn = load_from_json_file('add_item.json')
except:
    fn = open('add_item.json', 'w+')
    empty = []
    save_to_json_file(empty, 'add_item.json')
    fn.close()

temp = load_from_json_file('add_item.json')
if len(argv) > 0:
    for i in range(1, len(argv)):
        temp.append(argv[i])
    save_to_json_file(temp, 'add_item.json')
