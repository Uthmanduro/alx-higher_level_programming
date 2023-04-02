#!/usr/bin/python3
"""list 10 commits of a repository by user"""


import requests
import sys

if __name__ == "__main__":
    owner = sys.argv[2]
    repo = sys.argv[1]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=10"
    response = requests.get(url)
    for items in response.json():
        sha = items.get('sha')
        names = items.get('commit').get('author').get('name')
        print(f"{sha}: {names}")
