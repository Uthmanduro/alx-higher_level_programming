#!/usr/bin/python3
"""sends a request and displays the value of X-Request-Id variable"""


import urllib.request
import sys

url = sys.argv[1]
if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        print(response.info()['X-Request-Id'])
