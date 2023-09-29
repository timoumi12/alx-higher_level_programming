#!/usr/bin/python3
'''9-my_github.py'''


if __name__ == "__main__":
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    req = requests.get(url)
    req = req.json()
    for i in range(10):
        print("{}: {}".format(req[i].get("sha"),
                              req[i]["commit"]["author"].get("name")))
