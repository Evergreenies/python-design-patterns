# Filename      :       005_abstract_factory.py
# Created By    :       Suyog Shimpi
# Created Date  :       20/05/22
from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of product must implement this interface.
    """

    @abstractmethod
    def useful_method_a(self) -> str:  # noqa
        pass


class ConcreteProductA1(AbstractProductA):  # noqa
    def useful_method_a(self) -> str:  # noqa
        return 'The result of product A1'


class ConcreteProductA2(AbstractProductA):  # noqa
    def useful_method_a(self) -> str:  # noqa
        return 'This result of product A2'


class AbstractProdictB(ABC):
    """
    This is the another interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    """

    @abstractmethod
    def useful_method_b(self) -> str:
        """
        Product B is able to do its own things.
        :return:
        :rtype:
        """
        pass

    @abstractmethod
    def another_useful_method_b(self, collaborator: AbstractProductA) -> str:
        """
        But, it is also can collaborate with the ProductA.

        The abstract factory make sure that all products it creates are of the
        same variant and thus, compatible.
        :param collaborator:
        :type collaborator:
        :return:
        :rtype:
        """
        pass


class ConcreteProductB1(AbstractProdictB):  # noqa
    def useful_method_b(self) -> str:  # noqa
        return 'The result of product B1'

    def another_useful_method_b(self, collaborator: AbstractProductA) -> str:
        """
        The variant, Product B1, is only able to work correctly with the variant,
        Product A1. Nevertheless, it accepts ant instance of AbstractProductA as
        an argument
        :param collaborator:
        :type collaborator:
        :return:
        :rtype:
        """
        return f'The result of the B1 collaborating with the ' \
               f'({collaborator.useful_method_a()})'


class ConcreteProductB2(AbstractProdictB):  # noqa
    def useful_method_b(self) -> str:  # noqa
        return 'The result of the product B2'

    def another_useful_method_b(self, collaborator: AbstractProductA) -> str:
        """
        The variant, Product B2, is only able to work correctly with the variant,
        Product A2, Nevertheless, it accepts any instance of AbstractProductA as
        an argument.
        :param collaborator:
        :type collaborator:
        :return:
        :rtype:
        """
        return f'The result of B2 collaborating with the ' \
               f'({collaborator.useful_method_a()})'


class AbstractFactory(ABC):
    """
    The abstract factory declares a set of methods that return different abstract
    products. These products are called a family and are related by a high-level
    theme or concept. Products of one family are usually able to collaborate among
    themselves, A family of products may have several variants, but the product of
    one variant are incompatible with product of another.
    """

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:  # noqa
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProdictB:  # noqa
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Concrete factory produce a family of products that belong to a single variant.
    The factory guarantees that resulting products aer compatible.
    Note that, signatures of the concrete factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_product_a(self) -> AbstractProductA:  # noqa
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProdictB:  # noqa
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Each concrete factory has corresponding product variants.
    """

    def create_product_a(self) -> AbstractProductA:  # noqa
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProdictB:  # noqa
        return ConcreteProductB2()


def client_code(factory: AbstractFactory):
    """
    The client code works with factories and products only through abstract types:
    AbstractFactory and AbstractProduct. This lets you pass any factory or product
    subclass to the client code without breaking it.
    :param factory:
    :type factory:
    :return:
    :rtype:
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f'{product_b.useful_method_b()}')
    print(f'{product_b.another_useful_method_b(product_a)}')


if __name__ == '__main__':
    print('Client: Testing client code with the first factory type:')
    client_code(ConcreteFactory1())
    print()
    print('Client: Testing same client code with the second factory type:')
    client_code(ConcreteFactory2())
