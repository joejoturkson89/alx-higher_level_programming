#!/usr/bin/python3
"""This script takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        qVar = argv[1]
    else:
        qVar = ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': qVar})
    try:
        if r.json():
            print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
