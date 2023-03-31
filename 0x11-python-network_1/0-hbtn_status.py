#!/usr/bin/python3
"""fetches the given url"""


import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    result = response.read()
    print("Body response:")
    print(f"\ttype: {type(result)}")
    print(f"\tcontent: {result}")
    print(f"\tutf8 content: {result.decode('utf-8')}")
