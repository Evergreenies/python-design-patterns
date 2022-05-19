# Filename      :       001_ocp.py
# Created By    :       Suyog Shimpi
# Created Date  :       19/05/22

from enum import Enum
from typing import Generator


class Color(Enum):  # noqa
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):  # noqa
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    """A product"""

    def __init__(self, name: str, color: Color, size: Size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    """Product filter (Breaking OCP)"""

    def filter_by_color(self, products: list, color: Color) -> Generator:  # noqa
        """Filter product by colors"""
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products: list, size: Size) -> Generator:  # noqa
        """Filter product by size"""
        for p in products:
            if p.size == size:
                yield p

    def filter_by_color_and_size(self, products: list, color: Color, size: Size) -> Generator:  # noqa
        """Filter product by color and size"""
        for p in products:
            if p.color == color and p.size == size:
                yield p


"""
OCP pattern
"""


class Specification:
    """Enterprise Specification Design Pattern"""

    def is_satisfied(self, item):  # noqa
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    """Filter"""

    def filter(self, items, spec):  # noqa
        pass


class ColorSpecification(Specification):
    """Color specification"""

    def __init__(self, color: Color):
        self.color = color

    def is_satisfied(self, item) -> bool:  # noqa
        return item.color == self.color


class SizeSpecification(Specification):
    """Size specification"""

    def __init__(self, size: Size):
        self.size = size

    def is_satisfied(self, item) -> bool:  # noqa
        return item.size == self.size


class AndSpecification(Specification):
    """And specification"""

    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item) -> bool:  # noqa
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):
    """Advance filter"""

    def filter(self, items: list, spec) -> Generator:  # noqa
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    _products = [apple, tree, house]

    pf = ProductFilter()
    print('Green products (old): ')
    for _p in pf.filter_by_color(_products, Color.GREEN):
        print(f' - {_p.name}')

    bf = BetterFilter()
    print('Green products (new): ')
    green = ColorSpecification(Color.GREEN)
    for _p in bf.filter(_products, green):
        print(f' - {_p.name}')

    print('Large products: ')
    large = SizeSpecification(Size.LARGE)
    for _p in bf.filter(_products, large):
        print(f' - {_p.name}')

    print('Large-Blue items: ')
    large_blue = large and ColorSpecification(Color.BLUE)
    for _p in bf.filter(_products, large_blue):
        print(f' - {_p.name} is large and blue')
