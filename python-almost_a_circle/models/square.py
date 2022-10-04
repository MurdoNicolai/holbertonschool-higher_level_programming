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
