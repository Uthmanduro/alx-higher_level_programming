#!/usr/bin/python3
"""sends a post request with the email as parameter and displays the body"""


from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = parse.urlencode(value)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        result = response.read()
        print(result.decode('utf-8'))
