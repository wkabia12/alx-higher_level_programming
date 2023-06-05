#!/usr/bin/python3
'''
    Module defines Rectangle class
'''


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        height - height of recctangle
        width - width of recctangle
        number_of_instances - instances of Rectangle Class
        print_symbol - instances of Rectangle Class

    Methods:
        __init__ - initialize Rectangle objects
        __str__ - prints Rectangle string represntation
        __repr__ - prints Rectangle official string represntation
        __del__ - deletes Rectangle instance
        height - sets Rectangle height
        width - sets Rectangle width
        area - returns Rectangle area
        perimeter - returns Rectangle perimeter
        bigger_or_equal - returns bigest rectangle
        square - returns Rectangle instance that is square

    Description:
        The `Rectangle` class is used to define a Rectangle object.

    Example:
    >>> my_rect = Rectangle()
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initializes height and width """
        self.__height = 0
        self.__width = 0
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ prints representation of rectangle with # """
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        for i in range(self.__height):
            string += (str(self.print_symbol) * self.__width)
            if i < self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """ return representation of rectangle """
        return "Rectangle(" + str(self.__width) + ", "\
                            + str(self.__height) + ")"

    def __del__(self):
        """ deletion of instance """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def height(self):
        """ retrieve height """
        return self.__height

    @property
    def width(self):
        """ retrieve width """
        return self.__width

    @height.setter
    def height(self, value):
        """ set height with new value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """ set width with new value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @classmethod
    def square(cls, size=0):
        """ return an Rectangle instance that is a square """
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ bigger or equal instance """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def area(self):
        """ returns de area of rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ returns the perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)
