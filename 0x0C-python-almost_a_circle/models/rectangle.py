#!/usr/bin/python3
"""class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Class Description"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = 0

    @property
    def width(self):
        """Width Getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """"Width Setter"""

        self.validation("width", value)
        self.__width = value

    @property
    def height(self):
        """"Height Getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """Height Setter"""

        self.validation("height", value)
        self.__height = value

    @property
    def x(self):
        """x Getter"""

        return self.__x

    @x.setter
    def x(self, value):
        """x Setter"""

        self.validation("x", value)
        self.__x = value

    @property
    def y(self):
        """"y Getter"""

        return self.__y

    @y.setter
    def y(self, value):
        """y Setter"""

        self.validation("y", value)
        self.__y = value

    def validation(self, name, value, eq=True):
        """Validation method"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))
