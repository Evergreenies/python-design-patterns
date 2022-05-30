# Filename      :       002_strategy_example.py
# Created By    :       Suyog Shimpi
# Created Date  :       27/05/22
from abc import ABC, abstractmethod


class Strategy(ABC):
    """
    The Strategy interface declares operation common to all supported version of
    some algorithms.
    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def do_algorithm(self, data: list) -> list:  # noqa
        pass


class ConcreteStrategyA(Strategy):  # noqa
    def do_algorithm(self, data: list) -> list:  # noqa
        return sorted(data)


class ConcreteStrategyB(Strategy):  # noqa
    def do_algorithm(self, data: list):  # noqa
        return reversed(sorted(data))


class Context:
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but also
        provides a setter to change it at runtime.
        :param strategy:
        :type strategy:
        """
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of strategy. It should work
        with all strategies via a Strategy interface.
        :return:
        :rtype:
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        :param strategy:
        :type strategy:
        :return:
        :rtype:
        """
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        :return:
        :rtype:
        """
        print('Context: Sorting data using the strategy (not sure how it will do it)')
        result = self._strategy.do_algorithm(['a', 'b', 'c', 'd', 'e'])
        print(', '.join(result))


if __name__ == '__main__':
    _context = Context(ConcreteStrategyA())
    print('Client: Strategy is set to normal sorting.')
    _context.do_some_business_logic()
    print()
    print('Client: Strategy is set to reverse sorting.')
    _context.strategy = ConcreteStrategyB()
    _context.do_some_business_logic()
