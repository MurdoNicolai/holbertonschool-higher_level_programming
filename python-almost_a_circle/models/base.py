 #!/usr/bin/python3
""" contains the Base class """


class Base:
    """ Serves as Base for the other classes of the project:
        id (int): is diffrent for each object."""

    def __init__(self, id=None):
        __nb_objects = 0
        if id:
            id = id
        else:
            __nb_objects += 1
            id = __nb_objects


