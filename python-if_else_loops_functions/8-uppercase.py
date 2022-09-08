#!/usr/bin/python3
def uppercase(str):
    for c in str:
        c = ord(c)
        if c >= 97 and c < 123:
            c -= 32
        print(chr(c), end='')
    print()
