#!/usr/bin/python3
'''a script that fetches https://alx-intranet.hbtn.io/status'''


if __name__ = "__main__":
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        data = html.decode('utf-8')
        print('Body response:')
        print('    - type: {}'.format(type(html)))
        print('    - content: {}'.format(html))
        print('    - utf8 content: {}'.format(data))
