#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    num = 0
    import sys
    for args in sys.argv:
        num += int(args)
    print(f"{num}".format())
