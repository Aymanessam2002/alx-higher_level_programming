#!/usr/bin/python3
"""file"""
import sys
import json

def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

if __name__ == "__main__":
    args = ' '.join(sys.argv[1:]).split()
    item_list = load_from_json_file("add_item.json")

    if not args:
        print("Usage: ./7-add_item.py arg1 arg2 ...")
        sys.exit(1)

    item_list.extend(args)
    save_to_json_file(item_list, "add_item.json")

    print("Items added successfully.")



