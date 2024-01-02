#!/usr/bin/python3
"""
script that takes 2 arguments in order to list 10 commits (from the most
recent to oldest) of the repository "rails" by the user "rails".
Print all commits by: `<sha>: <author name>` (one by line)
The first argument will be the repository name
The second argument will be the owner name
"""
import requests
import sys


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        owner_name, repository_name)
    try:
        response = requests.get(url)
        commits = response.json()
        for i, obj in enumerate(commits):
            if i == 10:
                break
            if type(obj) is dict:
                name = obj.get('commit').get('author').get('name')
                print("{}: {}".format(obj.get('sha'), name))
    except Exception as invalid_json:
        pass
