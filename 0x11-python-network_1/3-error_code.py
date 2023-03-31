#!/usr/bin/python3
"""sends a request and displays a body of the response"""


from urllib import request, error
import sys

if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        response = request.urlopen(req)
        print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f'Error code: {e.code}')
