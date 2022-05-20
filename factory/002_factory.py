# Filename      :       002_factory.py
# Created By    :       Suyog Shimpi
# Created Date  :       20/05/22
import math


class Point(object):
    """Point class"""

    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'X: {self.x}, Y: {self.y}'

    class PointFactory:
        """Factory class to define creation of different object of point"""

        def new_cartesian_point(self, x: float, y: float):  # noqa
            """
            Method to create object of point for cartesian system
            :param x:
            :type x:
            :param y:
            :type y:
            :return:
            :rtype:
            """
            return Point(x, y)

        def new_polar_point(self, rho: float, theta: float):  # noqa
            """
            Object creation with polar system
            :param rho:
            :type rho:
            :param theta:
            :type theta:
            :return:
            :rtype:
            """
            return Point(rho * math.cos(theta), rho * math.sin(theta))

    factory = PointFactory()


if __name__ == '__main__':
    cartesian_point = Point(2, 3)
    print(cartesian_point)

    polar_point = Point.factory.new_polar_point(1, 2)
    print(polar_point)
