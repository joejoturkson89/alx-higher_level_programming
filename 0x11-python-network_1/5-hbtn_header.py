#!/usr/bin/python3
"""This script sends a request to the URL
and displays the value of the variable X-Request-Id in the response header."""

import requests
from sys import argv

if __name__ == "__main__":
    r = request.get(argv[1])
    print(r.headers.get('X-Request-Id'))
