#!/usr/bin/python3
"""takes in a letter and sends a post request """


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1 or type(sys.argv[1]) != str:
        param = ""
    else:
        param = sys.argv[1]
    try:
        response = requests.post('http://0.0.0.0:5000/search_user',
                                 data={'q': param})
        if response.json() == {}:
            print("No result")
        else:
            print(f"[{response.json()['id']}] {response.json()['name']}")
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")
