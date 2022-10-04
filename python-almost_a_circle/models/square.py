#!/usr/bin/python3
"""containse the square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a rectangle:
        __size (int): width of square
        __x (int): x postition on square
        __y (int): y postition on square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    size = Rectangle.width

    def update(self, *args, **kwargs):
        """alows update of the rectangle arg order: id, width, height x, y"""
        if len(args) > 0:
            super(Rectangle, self).__init__(args[0])
            if len(args) > 1:
                self.size = args[1]
                if len(args) > 2:
                    self.x = args[2]
                    if len(args) > 3:
                        self.y = args[3]
        else:
            try:
                super(Rectangle, self).__init__(kwargs['id'])
            except KeyError:
                pass
            try:
                self.width = kwargs['size']
            except KeyError:
                pass
            try:
                self.x = kwargs['x']
            except KeyError:
                pass
            try:
                self.y = kwargs['y']
            except KeyError:
                pass

    def to_dictionary(self):
        """ return the dictionary version of the rectangle"""
        self.dict = {'x': self.x, 'y': self.y, 'id': self.id,
                     'size': self.size}
        return self.dict
