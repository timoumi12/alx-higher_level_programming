#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    s = sum([int(i) for i in argv[1:]])
    print("{}".format(s))
