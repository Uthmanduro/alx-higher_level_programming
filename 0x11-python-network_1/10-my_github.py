#!/usr/bin/python3
"""takes mt github credential to display my id"""


import requests
import sys

if __name__ == "__main__":
    headers = {"X-GitHub-Api-Version": "2022-11-28",
               "Authorization":
               "Bearer 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"}
    response = requests.get("https://api.github.com/user", headers=headers)
    print(response.json()['id'])
