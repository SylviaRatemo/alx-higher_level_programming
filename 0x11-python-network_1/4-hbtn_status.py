#!/usr/bin/python3
"""urllib training"""
import urllib.request as url


with url.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()

print("Body response:\n\t- type: {}\n\t- content: {}".format(type(html), html))
