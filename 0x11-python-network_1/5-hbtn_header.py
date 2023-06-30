#!/usr/bin/python3
"""urllib training"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.header['X-Request-Id'])
