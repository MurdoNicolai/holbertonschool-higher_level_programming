#!/usr/bin/python3
""" test on modifying text file function """


def text_indentation(text):
    """ prints a string by adding 2 new lines after every . or ? or :
        text: string to print"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    text_update = str(text)
    after_new_line = False
    for c in text_update:
        if after_new_line:
            if c == " ":
                continue
            after_new_line = False
        if c == '.' or c == '?' or c == ':':
            print(c)
            print("")
            after_new_line = True
        else:
            print(c, end="")
