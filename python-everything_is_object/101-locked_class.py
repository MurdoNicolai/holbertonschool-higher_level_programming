#!/usr/bin/python3
"""
Creating a class that can only have 1 specifique attribute:
    LockedClass
"""
class LockedClass():
    """
        Prevent user frome creating an instance atribute other than first_name
    """
    def __getattribute__(self, key):
        if key != "first_name":
            raise AttributeError(f"'LockedClass' object has no attribute '{key}'")
    def __setattr__(self, key, value):
        if key != "first_name":
            raise AttributeError(f"'LockedClass' object has no attribute '{key}'")
        object.__setattr__(self, key, value)
    pass
