#!/usr/bin/python3
import sys
import json
import os
"""Add arguments to a python list"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

arg_list = []

if os.path.exists("add_item.json"):
    arg_list = load_from_json_file("add_item.json")

for i in range(1, len(sys.argv)):
    arg_list.append(sys.argv[i])

save_to_json_file(arg_list, "add_item.json")
