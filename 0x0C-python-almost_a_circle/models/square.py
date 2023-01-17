#!/usr/bin/python3
"""Defines the classsuqare that inherits from the class rectangle"""


from models.rectangle import Rectangle
"""import the rectangle module"""


class Square(Rectangle):
    """declares the square class that inherots from the rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns the string repr when the square object is printed"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """gets the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of size in the class"""
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """update the class by adding public method"""
        if len(args) != 0:
            count = 0
            for item in args:
                if count == 0:
                    if item is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = item
                elif count == 1:
                    self.size = item
                elif count == 2:
                    self.x = item
                elif count == 3:
                    self.y = item
                count += 1
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    Rectangle.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):

        """returns the dictionary representation of the sqaure class"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
