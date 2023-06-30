#!/usr/bin/python3
"""urllib training"""
import urllib.request as url


if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}".format(type(r.text), r.text))
