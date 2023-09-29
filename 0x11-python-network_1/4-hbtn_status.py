#!/usr/bin/python3
'''takes in a URL, sends a request to the URL and displays the response'''


if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(req)))
    print('\t- content: {}'.format(req))
