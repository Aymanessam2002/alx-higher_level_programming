#!/usr/bin/python3
"""file"""
import sys
import json
from os import path

def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    if not path.exists(filename):
        return []
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

if __name__ == "__main__":
    args = sys.argv[1:]
    item_list = load_from_json_file("add_item.json")

    if not args:
        print("Usage: ./7-add_item.py arg1 arg2 ...")
        sys.exit(1)

    item_list.extend(args)
    save_to_json_file(item_list, "add_item.json")

    print("Items added successfully.")


