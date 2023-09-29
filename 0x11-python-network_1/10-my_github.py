#!/usr/bin/python3
'''9-my_github.py'''


if __name__ == "__main__":
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    url = "https://api.github.com/user"
    username = sys.argv[1]
    pat = sys.argv[2]
    auth = HTTPBasicAuth(username, pat)
    req = requests.get(url, auth=auth)
    req = req.json()
    print("{}".format(req.get("id")))
