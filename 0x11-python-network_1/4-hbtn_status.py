#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with requests.get(url) as response:
        print("Body response:\n"
              "\t- type: {}\n"
              "\t- content: {}".format(type(response.text), response.text))
