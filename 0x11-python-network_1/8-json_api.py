#!/usr/bin/python3
"""requests training"""
import requests
import sys


if __name__ == "__main__":
    data = {"q": argv[1][0] if len(argv) > 1 else ""}
    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        r = r.json()
        if not r:
            print("No result")
        else:
            print("[{}] {}".format(r.get("id"), r.get("name")))
    except ValueError:
        print("Not a valid JSON")
