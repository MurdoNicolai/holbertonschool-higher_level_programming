#!/usr/bin/python3
"""adds all arguments to a python list then saves them to
    a file called add_item.json"""
import json
import sys
load_frome_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    newlist = load_frome_json_file("add_item.json")
except FileNotFoundError:
    newlist = list()
newlist.extend(sys.argv[1:])
save_to_json_file(newlist, "add_item.json")
