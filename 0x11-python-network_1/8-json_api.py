#!/usr/bin/python3
"""takes in a letter and sends a post request """


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1 or type(sys.argv) == str:
        q = ""
    else:
        response = requests.post('http://0.0.0.0:5000/search_user', data={'q': sys.argv[1]})
        print(response.status_code)
        if response.json() == None:
            print("No result")
        elif len(response.json()) > 1:
            print(f"[{response.json()['id']}] {response.json()['name']}")
        else:
            print("Not a valid JSON")
