#!/usr/bin/python3
"""send a request and sends the body of the response"""


import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
