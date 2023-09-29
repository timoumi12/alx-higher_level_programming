#!/usr/bin/python3
'''a script takes a URL,
 sends a request and displays the value of X-Request-Id found in the header'''


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        value = response.headers.get("X-Request-Id")
        print(value)
