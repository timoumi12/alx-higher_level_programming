#!/usr/bin/python3
'''8-json_api.py'''


if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    char = {'q': ""}
    if len(sys.argv) >= 2:
        char = {'q': sys.argv[1]}
    req = requests.post(url, data=char)
    try:
        req = req.json()
        if req == {}:
            print("No result")
        else:
            print("[{}] {}".format(req.get("id"), req.get("name")))
    except ValueError:
        print("Not a valid JSON")
