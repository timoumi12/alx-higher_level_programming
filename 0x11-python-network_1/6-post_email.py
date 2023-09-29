#!/usr/bin/python3
'''6-post_email.py'''


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    req = requests.post(url, params=email)
    print(req.text)
