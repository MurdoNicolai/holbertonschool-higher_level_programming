#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        c = None
    finally:
        try:
            print("Inside result: {:.1f}".format(c))
        except TypeError:
            print("Inside result: None")
    return c
