#!/usr/bin/python3
"""Defines a class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new instance of Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of
            the rectangle's position. Defaults to 0.
            y (int, optional): The y-coordinate of
            the rectangle's position. Defaults to 0.
            id (int, optional): The unique identifier
            for the rectangle. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter property for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the value is not a positive integer.

        """
        self.validation("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Getter property for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the value is not a positive integer.

        """
        self.validation("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Getter property for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute.

        Args:
            value (int): The x value to set.

        Raises:
            TypeError: If the value is not a non-negative integer.

        """
        self.validation("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter property for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute.

        Args:
            value (int): The y value to set.

        Raises:
            TypeError: If the value is not a non-negative integer.

        """
        self.validation("y", value)
        self.__y = value

    def validation(self, name, value, eq=True):
        """Method for validating an integer value.

        Args:
            name (str): The name of the value being
            validated, used in error messages.
            value (int): The value to be validated.
            eq (bool, optional): Whether the value
            should be greater than or equal to zero
            (default) or strictly greater than zero.

        Raises:
            TypeError: If the value is not of type int.
            ValueError: If the value does not meet
            the specified condition (non-negative or positive).

        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle,
            which is the product of its width and height.
        """
        return self.__width * self.__height

    def display(self):
        for _ in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def display(self):
        """Prints in stdout the Rectangle instance with the character #."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the instance
        based on positional and keyword arguments.

        Args:
            *args: Variable number of positional arguments.
            **kwargs: Variable number of keyword arguments.

        Note:
            This method allows updating attributes using a
            combination of both positional and keyword arguments.
        """
        if args and len(args) > 0:
            attr_list = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attr_list):
                    setattr(self, attr_list[i], value)

        if kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representation of the Rectangle instance.

        Returns:
            dict: A dictionary containing the attributes
            'id', 'width', 'height', 'x', and 'y'.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
