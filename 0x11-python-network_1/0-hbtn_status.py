#!/usr/bin/python3
"""urllib training"""
import urllib.request as url


with url.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()

print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
      .format(type(html), html, html.decode('utf-8')))
