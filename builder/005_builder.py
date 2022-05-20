# Filename      :       005_builder.py
# Created By    :       Suyog Shimpi
# Created Date  :       20/05/22
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """Abstract builder class"""

    @property
    @abstractmethod
    def product(self) -> None:  # noqa
        pass

    @abstractmethod
    def product_part_a(self) -> None:  # noqa
        pass

    @abstractmethod
    def product_part_b(self) -> None:  # noqa
        pass

    @abstractmethod
    def product_part_c(self) -> None:  # noqa
        pass


class ConcreteBuilder(Builder):
    """Concreate builder"""

    def __init__(self) -> None:
        self.reset()

    def reset(self):  # noqa
        self._product = Product1()  # noqa

    @property
    def product(self):  # noqa
        product = self._product
        self.reset()
        return product

    def product_part_a(self) -> None:  # noqa
        self._product.add('PARTA1')

    def product_part_b(self) -> None:  # noqa
        self._product.add('PARTB1')

    def product_part_c(self) -> None:  # noqa
        self._product.add('PARTC1')


class Product1:
    """Product"""

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:  # noqa
        self.parts.append(part)

    def list_parts(self) -> None:  # noqa
        print(f'Product parts: {", ".join(self.parts)}')


class Director:
    """Director is only responsible for executing the steps in particular sequence."""

    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Builder:  # noqa
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:  # noqa
        self.builder.product_part_a()

    def build_full_featured_product(self) -> None:  # noqa
        self.builder.product_part_a()
        self.builder.product_part_b()
        self.builder.product_part_c()


if __name__ == '__main__':
    _director = Director()
    _builder = ConcreteBuilder()
    _director.builder = _builder

    print('Standard basic product: ')
    _director.build_minimal_viable_product()
    _builder.product.list_parts()  # noqa

    print()
    print('Standard full featured product: ')
    _director.build_full_featured_product()
    _builder.product.list_parts()  # noqa

    print()

    print('Custom Product: ')
    _builder.product_part_a()
    _builder.product_part_c()
    _builder.product.list_parts()  # noqa
