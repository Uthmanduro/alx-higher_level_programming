#!/usr/bin/python3
"""sends a request and displays the value of variable in the response header"""


import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
