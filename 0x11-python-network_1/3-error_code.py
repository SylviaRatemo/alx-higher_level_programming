#!/usr/bin/python3
"""urllib training"""
import urllib.request as r
import sys


if __name__ == "__main__":
    try:
        with r.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e))
