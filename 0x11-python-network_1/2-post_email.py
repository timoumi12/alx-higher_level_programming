#!/usr/bin/python3
'''a script that fetches https://alx-intranet.hbtn.io/status'''
import urllib.request
import urllib.parse
import sys


if __name__ = "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii') # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        resp = response.read()
        data = resp.decode('utf-8')
        print(data)
