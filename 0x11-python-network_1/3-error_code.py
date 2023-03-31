#!/usr/bin/python3
"""sends a request and displays a body of the response"""


import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        response = urllib.request.urlopen(req)
        print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
