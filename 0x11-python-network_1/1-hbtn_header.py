#!/usr/bin/python3
"""urllib training"""
import urllib.request as url
import sys


with url.urlopen(sys.argv[1]) as response:
    pass

print(response.headers["X-Request-Id"])
