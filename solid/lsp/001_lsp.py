# Filename      :       001_lsp.py
# Created By    :       Suyog Shimpi
# Created Date  :       19/05/22


class Rectangle:
    """Rectangle"""

    def __init__(self, width: float, height: float):
        self._height = height
        self._width = width

    @property
    def area(self) -> float:
        """Finding area of rectangle"""
        return self._width * self._height

    @property
    def width(self):  # noqa
        return self._width

    @width.setter
    def width(self, value: float):
        self._width = value

    @property
    def height(self):  # noqa
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = value

    def __str__(self) -> str:
        return f'Width: {self.width}, Height: {self.height}'


class Square(Rectangle):
    """Square class"""

    def __init__(self, size: float):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value: float):  # noqa
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value: float):  # noqa
        self._width = self._height = value


def use_it(rc):  # noqa
    expected = int(rc.width * rc.height)
    print(f'Expected an area of {expected}, got {rc.area}')


if __name__ == '__main__':
    _rc = Rectangle(2, 3)
    use_it(_rc)

    _sq = Square(5)
    use_it(_sq)
