#!/usr/bin/python3
"""Module for the rectangle class that inherits from Base class"""


from models.base import Base
"""imports the base function"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Defines the recatngle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(id)

    @property
    def width(self):
        """gets the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """gets the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """getd the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints the rectangle instance with the character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        for line in range(self.y):
            print()
        for row in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """returs the string representation of the object"""
        return "[Rectangle] (" + str(self.id) + ") " + str(self.x) + "/" +\
               str(self.y) + " - " + str(self.width) + "/" + str(self.height)

    def update(self, *args, **kwargs):
        """update the rectangle by assigning an argument to each variable"""
        if len(args) != 0:
            count = 0
            for item in args:
                if count == 0:
                    if item is None:
                        self.__init__(self.id, self.width, self.height,
                                      self.x, self.y)
                    else:
                        self.id = item
                elif count == 1:
                    self.width = item
                elif count == 2:
                    self.height = item
                elif count == 3:
                    self.x = item
                elif count == 4:
                    self.y = item
                count += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a rectangle"""
        return {"id": self.id, "width": self.width, "height": self.height, "x":
                self.x, "y": self.y}
