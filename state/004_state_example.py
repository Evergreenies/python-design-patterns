# Filename      :       004_state_example.py
# Created By    :       Suyog Shimpi
# Created Date  :       27/05/22
from abc import ABC, abstractmethod


class State(ABC):
    """
    The base state class declares methods that all Concrete State should
    implement and also provides a back-reference to Context object, associated
    with the State. This back-reference can also be used by States to transition
    the context to another state.
    """

    @property
    def context(self) -> None:  # noqa
        return self._context

    @context.setter
    def context(self, context) -> None:  # noqa
        self._context = context  # noqa

    @abstractmethod
    def handle1(self) -> None:  # noqa
        pass

    @abstractmethod
    def handle2(self) -> None:  # noqa
        pass


class ConcreteStateA(State):  # noqa
    def handle1(self) -> None:  # noqa
        print('ConcreteStateA: handles request1.')
        print('ConcreteStateA: wants to change the state of the context.')
        self.context.transition_to(ConcreteStateB())  # noqa

    def handle2(self) -> None:  # noqa
        print('ConcreteStateA: handles request2.')


class ConcreteStateB(State):  # noqa
    def handle1(self) -> None:  # noqa
        print('ConcreteStateB: handles request1.')

    def handle2(self) -> None:  # noqa
        print('ConcreteStateB: handles request2.')
        print('ConcreteStateB: wants to change the state of the context.')
        self.context.transition_to(ConcreteStateA())  # noqa


class Context:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """
    _state = None  # reference to the current state of the context.

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State) -> None:
        """
        The Context allows changing the State object at runtime.
        :param state:
        :type state:
        :return:
        :rtype:
        """
        print(f'Context: Transition to {type(state).__name__}')
        self._state = state
        self._state.context = self

    def request1(self) -> None:  # noqa
        self._state.handle1()

    def request2(self) -> None:  # noqa
        self._state.handle2()


if __name__ == '__main__':
    _context = Context(ConcreteStateA())
    _context.request1()
    print()
    _context.request2()
