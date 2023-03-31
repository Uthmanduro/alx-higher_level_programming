#!/usr/bin/python3
"""fetches the given url"""


import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        result = res.read()
        print("Body response:")
        print(f"\t- type: {type(result)}")
        print(f"\t- content: {result}")
        print(f"\t- utf8 content: {result.decode('utf-8')}")
