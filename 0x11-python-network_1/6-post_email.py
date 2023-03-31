#!/usr/bin/python3
"""takes in a email and url and send a post request to the url"""


import requests
import sys

if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(response.text)
