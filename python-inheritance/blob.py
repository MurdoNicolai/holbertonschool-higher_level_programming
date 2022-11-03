#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute

class MyClass():
    pass

class LockedClass():
    """
        Prevent user frome creating an instance atribute other than first_name
    """

    def __getattribute__(self, key):
        if key != "first_name":
            raise AttributeError(f"'LockedClass' object"
                                f" has no attribute '{key}'")
        pass

    def __setattr__(self, key, value):
        if key != "first_name":
            raise AttributeError(f"'LockedClass' object"
                                 f" has no attribute '{key}'")
        object.__setattr__(self, key, value)
    pass

print(LockedClass().__dict__)

try:
    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    mc = LockedClass()
    add_attribute(mc, "first_name", "John")
    print(mc.first_name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    a = {"grg" : 5}
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
