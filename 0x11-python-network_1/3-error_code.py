#!/usr/bin/python3
"""This script takes in a URl,
sends a request to the URl and
displays the body of the response(decode in utf-8)"""

if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
