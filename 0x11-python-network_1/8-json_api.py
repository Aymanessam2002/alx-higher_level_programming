#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q.
If no argument is given, set q="".
If the response body is properly JSON formatted and not empty, display the
id and name like this: [<id>] <name>, Otherwise: Display Not a valid JSON
if the JSON is invalid and Display No result if the JSON is empty
"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    try:
        req = requests.post(url, data={'q': q})
        json_data = req.json()
        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError as invalid_json:
        print("Not a valid JSON")
