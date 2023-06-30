#!/usr/bin/python3
""" Github code challenge"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"\
          .format(sys.argv[2], sys.argv[1])
    r = requests.get(url)
    count = 0
    for i in r.json():
        if count < 10:
            print("{}: {}".format(i.get("sha"),
                  i.get("commit").get("author").get("name")))
        count+=1
