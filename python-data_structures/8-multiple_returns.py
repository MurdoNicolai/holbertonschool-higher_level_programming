#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    firstchar = ''
    if length != 0:
        firstchar = sentence[0]
    else:
        return 0, None
    return length, firstchar
