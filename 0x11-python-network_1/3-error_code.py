#!/usr/bin/python3
'''takes in a URL, sends a request to the URL and displays the response'''


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            resp = response.read()
            data = resp.decode('utf-8')
            print(data)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
        return
