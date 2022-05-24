# Filename      :       class_decorator.py
# Created By    :       Suyog Shimpi
# Created Date  :       24/05/22
from abc import ABC


class Shape(ABC):
    def __str__(self):
        return ''


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'A circle of radius {self.radius}'


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'A square with side {self.side}'


class ColoredShape(Shape):
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def __str__(self):
        return f'{self.shape} has the color {self.color}'


class TransparencyShape(Shape):
    def __init__(self, shape, transparency):
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f'{self.shape} has {self.transparency * 100} transparency.'


if __name__ == '__main__':
    _circle = Circle(2)
    print(_circle)

    red_circle = ColoredShape(_circle, 'red')
    print(red_circle)

    red_half_transparent_circle = TransparencyShape(
        red_circle, .5
    )
    print(red_half_transparent_circle)
