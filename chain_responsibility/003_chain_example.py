# Filename      :       003_chain_example.py
# Created By    :       Suyog Shimpi
# Created Date  :       25/05/22
from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    """
    The handler interface declares a method for building the chain of handlers. It
    also declares a method for executing requests.
    """

    @abstractmethod
    def set_next(self, handler):  # noqa
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:  # noqa
        pass


class AbstractHandler(Handler):
    """
    The default chaining behaviour can be implemented inside a base handler class.
    """
    _next_handler = None

    def set_next(self, handler) -> Handler:
        """
        Returning a handler from here will let us link handlers in a convenient
        way like this:
        monkey.set_next(squirrel).set_next(dog)

        :param handler:
        :type handler:
        :return:
        :rtype:
        """
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request) -> Optional[str]:  # noqa
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class MonkeyHandler(AbstractHandler):  # noqa
    def handle(self, request) -> Optional[str]:  # noqa
        if request == 'Banana':
            return f'Monkey: I will eat the {request}'
        else:
            super(MonkeyHandler, self).handle(request)


class SquirrelHandler(AbstractHandler):  # noqa
    def handle(self, request) -> Optional[str]:  # noqa
        if request == 'Nut':
            return f'Squirrel: I will eat the {request}'
        else:
            return super(SquirrelHandler, self).handle(request)


class DogHandler(AbstractHandler):  # noqa
    def handle(self, request) -> Optional[str]:  # noqa
        if request == 'MeatBall':
            return f'Dog: I will eat the {request}'
        else:
            return super(DogHandler, self).handle(request)


def client_code(handler: Handler) -> None:  # noqa
    for food in ['Nut', 'Banana', 'Cup of coffee']:
        print(f'\nClient: Who wants a `{food}`?')
        result = handler.handle(food)
        if result:
            print(f'    {result}', end='')
        else:
            print(f'    `{food}` was left untouched.', end='')


if __name__ == '__main__':
    _monkey = MonkeyHandler()
    _squirrel = SquirrelHandler()
    _dog = DogHandler()

    _monkey.set_next(_squirrel).set_next(_dog)

    print()
    print('Chain ==> ⛓ : Monkey🐒 > Squirrel🐿 > Dog🐕')
    client_code(_monkey)
    print()
    print('Sub-chain ==> ⛓ : Squirrel🐿 > Dog🐕')
    client_code(_squirrel)
