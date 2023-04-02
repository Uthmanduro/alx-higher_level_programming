#!/usr/bin/python3
"""takes mt github credential to display my id"""


import requests
import sys

if __name__ == "__main__":
    token = sys.argv[2]
    headers = {"X-GitHub-Api-Version": "2022-11-28",
               "Authorization": f"{token}",
               "Accept": "application/vnd.github+json"}
    response = requests.get("https://api.github.com/user", headers=headers,
                            auth=(sys.argv[1], sys.argv[2]))
    print(response.json().get('id'))
