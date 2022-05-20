# Filename      :       004_factory_methods.py
# Created By    :       Suyog Shimpi
# Created Date  :       20/05/22
from abc import ABC, abstractmethod


class Product(ABC):
    """The product interface declares tje operations that all concrete products must implement"""

    @abstractmethod
    def operation(self) -> str:  # noqa
        pass


class ConcreteProduct1(Product):  # noqa
    def operation(self) -> str:  # noqa
        return 'Result of concrete product 1'


class ConcreteProduct2(Product):  # noqa
    def operation(self) -> str:  # noqa
        return 'Result of concrete product 2'


class Creator(ABC):
    """
    The creator class declares the factory method that is supposed to return an
    object of a product class.
    """

    @abstractmethod
    def factory_method(self):  # noqa
        pass

    def some_operation(self) -> str:  # noqa
        product = self.factory_method()
        return f'Creator: The same creator`s code has just worked with {product.operation()}'


class ConcreteCreator1(Creator):  # noqa
    def factory_method(self):  # noqa
        return ConcreteProduct1()


class ConcreteCreator2(Creator):  # noqa
    def factory_method(self):  # noqa
        return ConcreteProduct2()


def client_code(creator: Creator) -> None:  # noqa
    print(f'Client: I`m not aware of the creator`s class, but it still works.\n'
          f'{creator.some_operation()}')


if __name__ == '__main__':
    print('App: Launched with the ConcreteCreator1')
    client_code(ConcreteCreator1())
    print()
    print('App: Launched with the ConcreteCreator2')
    client_code(ConcreteCreator2())
