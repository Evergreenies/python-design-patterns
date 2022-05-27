# Filename      :       002_command_example.py
# Created By    :       Suyog Shimpi
# Created Date  :       25/05/22
from abc import ABC, abstractmethod


class Command(ABC):
    """
    This command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self) -> None:  # noqa
        pass


class SimpleCommand(Command):
    """
    Some command can implement simple operations on their own.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:  # noqa
        print(f'SimpleCommand: See, I can do simple things like printing ({self._payload})')


class Receiver:
    """
    The Receiver classes contain some important business logic. They know how to perform
    all kinds of operations, associated with carrying out a request. In fact, any class
    may serve as a Receiver.
    """

    def do_something(self, a: str) -> None:  # noqa
        print(f'\nReceiver: Working on ({a}.)')

    def do_something_else(self, b: str) -> None:  # noqa
        print(f'\nReceiver: Also working on ({b}.)')


class ComplexCommand(Command):
    """
    However, some command can delegate more complex operations to other
    objects, called `receivers`.
    """

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        self._b = b
        self._a = a
        self._receiver = receiver

    def execute(self) -> None:
        """
        Commands can delegate to any methods of a receiver.
        :return:
        :rtype:
        """
        print('ComplexCommand: Complex stuff should be done by a receiver object')
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Invoker:
    """
    The invoker is associated with one or several commands. It sends a request to
    the command.
    """

    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command) -> None:  # noqa
        self._on_start = command

    def set_on_finish(self, command: Command) -> None:  # noqa
        self._on_finish = command

    def do_something_important(self) -> None:  # noqa
        """
        The Invoker does not depend on concrete command or receiver classes. The
        Invoker passes a request to a receiver indirectly, b executing a command.
        :return:
        :rtype:
        """

        print('Invoker: Does anybody want something done before I begin?')
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print('Invoker: .. doing something really important...')
        print('Invoker: Does anybody want something dene before I finish?')
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == '__main__':
    _invoker = Invoker()
    _invoker.set_on_start(SimpleCommand('Say Hi!'))
    _receiver = Receiver()
    _invoker.set_on_finish(
        ComplexCommand(_receiver, 'Send email', 'Save report')
    )
    _invoker.do_something_important()
