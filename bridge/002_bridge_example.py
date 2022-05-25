# Filename      :       002_bridge_example.py
# Created By    :       Suyog Shimpi
# Created Date  :       25/05/22

from abc import ABC, abstractmethod


class Implementation(ABC):
    """
    The implementation defines the interface for all implementation classes. It doesn't
    have to match the abstraction's interface. In fact, the two interfaces can be entirely
    different. Typically, the implementation interface provides only primitive operations,
    while the abstraction defines higher-level operations based on those primitives.
    """

    @abstractmethod
    def operation_implementation(self) -> str:  # noqa
        pass


class ConcreteImplementationA(Implementation):  # noqa
    def operation_implementation(self) -> str:  # noqa
        return 'ConcreteImplementationA: Here`s the result on the platform A.'


class ConcreteImplementationB(Implementation):  # noqa
    def operation_implementation(self) -> str:  # noqa
        return 'ConcreteImplementationB: Here`s the result on th platform B.'


class Abstraction:
    """
    The abstraction defines the interface for the control part of the two class hierarchies.
    It maintains a reference to an object of the implementation hierarchy and delegates all
    the real work to this object.
    """

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:  # noqa
        return f'Abstraction: Base operation with:\n' \
               f'{self.implementation.operation_implementation()}'


if __name__ == '__main__':
    _implementation = ConcreteImplementationA()
    _abstraction = Abstraction(_implementation)
    print(_abstraction.operation())

    print()
    _implementation = ConcreteImplementationB()
    _abstraction = Abstraction(_implementation)
    print(_abstraction.operation())
