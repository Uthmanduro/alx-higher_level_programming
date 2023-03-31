#!/usr/bin/python3
"""sends a post request with the email as parameter and displays the body"""


import urllib.request
import urllib.parse
import sys

if __name__ = "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        result = response.read()
        print(result.decode('utf-8'))
