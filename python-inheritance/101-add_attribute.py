#!/usr/bin/python3
"""adding test if attribute can be added"""


def add_attribute(object, key, value):
    """basacly we just see if object has __dict__ then add it if it has"""
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, key, value)
