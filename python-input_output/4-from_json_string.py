#!/usr/bin/python3
#!/usr/bin/python3
"""has function that returns the object frome JSON representation"""
import json


def from_json_string(my_str):
    """returns the object representation of:
        my_str (string)
    """
    return json.loads(my_str)
