#!/usr/bin/python3
"""class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Class Description"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor
        Attributes:
            width (int): Rectangle width
            height (int): Rectangle height
            x (int): x coordinate
            y (int): y coordinate
            id (int): identity of rectangle
        Raises:
            ValueError: width or height <= 0, x or y < 0
            TypeError: widh, height, x, y not int
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width Getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """"Width Setter"""

        self.validation("width", value, False)
        self.__width = value

    @property
    def height(self):
        """"Height Getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """Height Setter"""

        self.validation("height", value, False)
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

    def validation(self, name, value, opt=True):
        """Validation method"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if opt and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not opt and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """Method computing the area"""

        return self.__width * self.__height

    def display(self):
        """Method to print Rectangle using #"""

        if self.width == 0 or self.height == 0:
            print("")
            return
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        """String magic method"""

        name = type(self).__name__
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(name, self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assign argument to attributes"""

        count = 0
        for i in args:
            count += 1
            if count == 1:
                self.id = i
            elif count == 2:
                self.width = i
            elif count == 3:
                self.height = i
            elif count == 4:
                self.x = i
            elif count == 5:
                self.y = i

        if len(args) == 0:
            for key, value in kwargs.items():
                if key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value

    def to_dictionary(self):
        """Dictionary representation of Rectangle"""

        return {"id": self.id, "width": self.width, "height":
                self.height, "x": self.x, "y": self.y}
