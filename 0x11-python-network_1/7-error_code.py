#!/usr/bin/python3
'''7-error_code.py'''


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    try:
        req = requests.get(url)
    except req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    print(req.text)
