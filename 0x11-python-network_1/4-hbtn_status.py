#!/usr/bin/python3
"""urllib training"""
import urllib.request as url


if __name__ == "__main__":
    with url.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:\n\t- type: {}\n\t- content: {}"
              .format(type(html.text), html.text))
