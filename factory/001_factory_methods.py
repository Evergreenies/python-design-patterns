# Filename      :       001_factory_methods.py
# Created By    :       Suyog Shimpi
# Created Date  :       20/05/22
import math


class Point:
    def __init__(self, x: float, y: float):
        self.y = y
        self.x = x

    @staticmethod
    def new_cartesian_point(x: float, y: float):  # noqa
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho: float, theta: float):  # noqa
        return Point(rho * math.cos(theta), theta * math.sin(theta))

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'


if __name__ == '__main__':
    point = Point(2, 3)
    point2 = Point.new_polar_point(1, 2)
    print(point, point2)
