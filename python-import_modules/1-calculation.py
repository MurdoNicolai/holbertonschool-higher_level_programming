#!/usr/bin/python3
if __name__ == "__main__":
    from audioop import mul
    from re import sub
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    print(f"{a} + {b} = {add(a,b)}".format())
    print(f"{a} - {b} = {sub(a,b)}".format())
    print(f"{a} * {b} = {mul(a,b)}".format())
    print(f"{a} / {b} = {div(a,b)}".format())
