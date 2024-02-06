#!/usr/bin/python3
"""Script to add arguments to a Python list and save them to a JSON file."""
import sys
import json
from os import path

def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    if not path.exists(filename):
        return []
    with open(filename, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    args = sys.argv[1:]
    item_list = load_from_json_file("add_item.json")
    item_list.extend(args)
    save_to_json_file(item_list, "add_item.json")




