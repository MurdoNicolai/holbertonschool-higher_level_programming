#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is ".format(), end='')
number = abs(number) % 10
if number > 5:
    print(f"{number} and is greater than 5".format())
elif number == 0:
    print(f"{number} and is 0".format())
else:
    print(f"{number} and is less than 6 and not 0".format())
