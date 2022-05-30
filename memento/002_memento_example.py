# Filename      :       002_memento_example.py
# Created By    :       Suyog Shimpi
# Created Date  :       26/05/22
import datetime
from abc import ABC, abstractmethod
from random import sample
from string import ascii_letters


class Memento(ABC):
    """
    The Memento interface provides a way to retrieve the memento's metadata, such
    as creation data or name. However, it doesn't expose the originator's state.
    """

    @abstractmethod
    def get_name(self) -> str:  # noqa
        pass

    @abstractmethod
    def get_date(self) -> str:  # noqa
        pass


class ConcreteMemento(Memento):  # noqa
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.datetime.now())[:19]

    def get_state(self) -> str:  # noqa
        """
        The originator uses this method when restoring its state.
        :return:
        :rtype:
        """
        return self._state

    def get_name(self) -> str:  # noqa
        return f'{self._date} / ({self._state[:9]}...)'

    def get_date(self) -> str:  # noqa
        return self._date


class Originator:
    """
    The originator holds some important state that may change over tome. It also
    defines a method for saving the state inside a memento and another method for
    restoring the state from it.
    """
    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f'Originator: My initial state is: {self._state}')

    def _generate_random_string(self, length: int = 10) -> str:  # noqa
        return ''.join(sample(ascii_letters, length))

    def do_something(self) -> None:
        """
        The originators business logic may affect its internal state. Therefore,
        the client should back up the state before launching methods of the
        business logic via the save() method.
        :return:
        :rtype:
        """
        print('Originator: I`m doing something important.')
        self._state = self._generate_random_string(30)
        print(f'Originator: and my state has changes to: {self._state}')

    def save(self) -> Memento:
        """
        Save the current state inside memento.
        :return:
        :rtype:
        """
        return ConcreteMemento(self._state)

    def restore(self, memento: ConcreteMemento) -> None:
        """
        Restores the Originator's state from a memento object.
        :param memento:
        :type memento:
        :return:
        :rtype:
        """
        self._state = memento.get_state()
        print(f'Originator: My state has changed to: {self._state}')


class Caretaker:
    """
    The Caretaker doesn't depend on the concrete memento class. Therefore, it
    doesn't have access to the originator's state, stored inside the memento.
    It works with all mementos via the base memento interface.
    """

    def __init__(self, originator: Originator) -> None:
        self._memento = []
        self._originator = originator

    def backup(self) -> None:  # noqa
        print('\nCaretaker: Saving originators state...')
        self._memento.append(self._originator.save())

    def undo(self) -> None:  # noqa
        if not len(self._memento):
            return
        memento = self._memento.pop()
        print(f'Caretaker: Restoring state to: {memento.get_name()}')
        try:
            self._originator.restore(memento)
        except Exception:  # noqa
            self.undo()

    def show_history(self) -> None:  # noqa
        print('Caretaker: Here`s the list of mementos:')
        for memento in self._memento:
            print(memento.get_name())


if __name__ == '__main__':
    _originator = Originator('super-duper')
    _caretaker = Caretaker(_originator)

    _caretaker.backup()
    _originator.do_something()

    _caretaker.backup()
    _originator.do_something()

    _caretaker.backup()
    _originator.do_something()

    print()
    _caretaker.show_history()

    print()
    print('Now, let`s rollback!')
    _caretaker.undo()
    print('One more time...')
    _caretaker.undo()
