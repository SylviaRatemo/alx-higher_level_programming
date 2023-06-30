#!/usr/bin/python3
"""urllib training"""
import urllib.request as url
import sys


if __name__ == "__main__":
    with url.urlopen(sys.argv[1]) as response:
        print(response.headers["X-Request-Id"])
