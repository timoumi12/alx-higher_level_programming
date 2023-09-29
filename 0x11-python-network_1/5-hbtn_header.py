#!/usr/bin/python3
'''5-hbtn_header.py'''


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    req = requests.get(url)
    data = req.headers["X-Request-Id"]
    print(data)
