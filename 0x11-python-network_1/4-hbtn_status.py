#!/usr/bin/python3
'''takes in a URL, sends a request to the URL and displays the response'''


if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)
    txt = req.text
    print('Body response:')
    print('\t- type: {}'.format(type(txt)))
    print('\t- content: {}'.format(txt))
