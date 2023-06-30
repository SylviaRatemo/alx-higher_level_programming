#!/usr/bin/python3
"""urllib training"""
import urllib.parse as p
import urllib.request as r
import sys


if __name__ == "__main__":
    data = p.urlencode({"email": sys.argv[2]}).encode()
    with r.urlopen(sys.argv[1], data) as response:
        html = response.read()
        print(html.decode('utf-8'))
