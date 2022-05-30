# Filename      :       003_mediator_example.py
# Created By    :       Suyog Shimpi
# Created Date  :       26/05/22
from abc import ABC


class Mediator(ABC):
    """
    The Mediator interface declares a method used by components to notify the
    mediator about various events. The Mediator may react to these events and
    pass the execution to another component.
    """

    def notify(self, sender: object, event: str) -> None:  # noqa
        pass


class BaseComponent:
    """
    This class provides basic functionality of storing a mediator's instance
    inside component objects.
    """

    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:  # noqa
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:  # noqa
        self._mediator = mediator


class Component1(BaseComponent):  # noqa
    def do_a(self) -> None:  # noqa
        print('Component1 does A.')
        self.mediator.notify(self, 'A')

    def do_b(self) -> None:  # noqa
        print('Component1 does B.')
        self.mediator.notify(self, 'B')


class Component2(BaseComponent):  # noqa
    def do_c(self) -> None:  # noqa
        print('Component2 does C.')
        self.mediator.notify(self, 'C')

    def do_d(self) -> None:  # noqa
        print('Component2 does D.')
        self.mediator.notify(self, 'D')


class ConcreteMediator(Mediator):  # noqa
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:  # noqa
        if event == 'A':
            print('Mediator reacts on A and triggers following operations:')
            self._component2.do_c()
        elif event == 'D':
            print('Mediator reacts on D and triggers following operations:')
            self._component1.do_b()
            self._component2.do_c()


if __name__ == '__main__':
    c1 = Component1()
    c2 = Component2()

    _mediator = ConcreteMediator(c1, c2)
    print('Client triggers operation A.')
    c1.do_a()

    print()
    print('Client triggers operation D.')
    c2.do_d()
