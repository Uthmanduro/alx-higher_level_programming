#!/usr/bin/python3
"""sends a request and displays the value of X-Request-Id variable"""


from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
