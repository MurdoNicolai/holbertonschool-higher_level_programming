#!/usr/bin/python3
for i in range(26):
    if i % 2 == 1:
        i += 32
    print(chr(122 - i), end='')
    if i % 2 == 1:
        i -= 32
