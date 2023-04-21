#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class description"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Magic method string"""

        name = type(self).__name__
        return '[{}] ({}) {}/{} - {}'.\
            format(name, self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """Size Getter"""

        return self.width

    @size.setter
    def size(self, value):
        """size Setter"""

        super().validation("width", value, False)
        self.width = value
        self.height = value
