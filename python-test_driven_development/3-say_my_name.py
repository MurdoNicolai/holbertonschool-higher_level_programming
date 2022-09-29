#!/usr/bin/python3
""" now se write a simple funcion with words for testing """


def say_my_name(first_name, last_name=""):
    """ prints a sentance followed by first and last name:
        first_name: self evident
        last_name: self evident """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
