# Filename      :       003_protection_proxy.py
# Created By    :       Suyog Shimpi
# Created Date  :       25/05/22
from abc import ABC, abstractmethod


class Subject(ABC):
    """
    The Subject interface declares common operations for both RealSubject and
    the Proxy. As long as the client works with RealSubject using this interface,
    you will be able to pass it to a proxy instead of a real subject.
    """

    @abstractmethod
    def request(self) -> None:  # noqa
        pass


class RealSubject(Subject):
    """
    The RealSubject contains some core business logic. Usually, RealSubject are
    capable of doing some useful work which may also be very slow or sensitive -
    ex. - correcting input data. A proxy can solve issues without any changes to
    the RealSubject's code.
    """

    def request(self) -> None:  # noqa
        print('RealSubject: Handling request.')


class Proxy(Subject):  # noqa
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def check_access(self) -> bool:  # noqa
        print('Proxy: Checking access prior to firing a real request.')
        return True

    def log_access(self) -> None:  # noqa
        print('Proxy: Encountered request.')

    def request(self) -> None:  # noqa
        """
        The most common application of the Proxy pattern are lazy loading,
        controlling the access, logging, etx. A Proxy can perform one of
        these things and then, depending on the result, pass the execution
        to the same method in linked RealSubject object.
        :return:
        :rtype:
        """
        if self.check_access():
            self._real_subject.request()
            self.log_access()


if __name__ == '__main__':
    print('Client: Executing the client code with a real subject:')
    _real_subject = RealSubject()
    _real_subject.request()

    print()
    print('Client: Executing the same client code with a proxy:')
    _proxy = Proxy(_real_subject)
    _proxy.request()
