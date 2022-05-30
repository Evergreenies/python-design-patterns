# Filename      :       003_observer_example.py
# Created By    :       Suyog Shimpi
# Created Date  :       26/05/22
import random
from abc import ABC, abstractmethod
from typing import Any, List


class Observer(ABC):
    """
    This interface declares the update method, used by another classes.
    """

    @abstractmethod
    def update(self, subject: Any) -> None:
        """
        Receive update from another consumers.
        :param subject:
        :type subject:
        :return:
        :rtype:
        """
        pass


class Subject(ABC):
    """
    This interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach observer to the subscriber.
        :param observer:
        :type observer:
        :return:
        :rtype:
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach observer from the subscriber.
        :param observer:
        :type observer:
        :return:
        :rtype:
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        :return:
        :rtype:
        """
        pass


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state = None
    _observers: List = []

    def attach(self, observer: Observer) -> None:  # noqa
        print(f'Subject: Attach an observer - {type(observer).__name__}')
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:  # noqa
        print(f'Subject: Detached an observer - {type(observer).__name__}')
        self._observers.remove(observer)

    def notify(self) -> None:
        """
        Trigger an event in each subscriber.
        :return:
        :rtype:
        """
        print(f'Subject: Notifying observers...')
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important about to
        happen (or after it).
        :return:
        :rtype:
        """
        print()
        print('Subject: I`m doing something important.')
        self._state = random.randrange(0, 10)

        print()
        print(f'Subject: My state has just changes to: {self._state}')
        self.notify()


class ConcreteObserverA(Observer):  # noqa
    def update(self, subject: Any) -> None:  # noqa
        if subject._state < 3:  # noqa
            print('ConcreteObserverA: Reacted to the event.')


class ConcreteObserverB(Observer):  # noqa
    def update(self, subject: Any) -> None:  # noqa
        if subject._state == 0 or subject._state >= 2:  # noqa
            print('ConcreteObserverB: Reacted to the event.')


if __name__ == '__main__':
    _subject = ConcreteSubject()
    observer_a = ConcreteObserverA()
    _subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    _subject.attach(observer_b)

    _subject.some_business_logic()
    _subject.some_business_logic()

    _subject.detach(observer_a)

    _subject.some_business_logic()
