#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    i = 0
    import sys
    print(f"{len(argv)} arguments:".format())

    for args in sys.argv:
        i += 1
        print(f"{i}: {args}".format())
