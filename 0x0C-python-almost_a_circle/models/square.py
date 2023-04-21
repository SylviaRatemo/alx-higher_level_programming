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

    def update(self, *args, **kwargs):
        """method to assign attributes"""

        count = 0
        for i in args:
            count += 1
            if count == 1:
                self.id = i
            elif count == 2:
                self.width = i
            elif count == 3:
                self.x = i
            elif count == 4:
                self.y = i

        if len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
