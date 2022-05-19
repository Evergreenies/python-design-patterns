# Filename      :       001_isp.py
# Created By    :       Suyog Shimpi
# Created Date  :       19/05/22

from abc import abstractmethod, ABC


class Machine:
    def print(self, document):
        raise NotImplemented

    def fax(self, document):
        raise NotImplemented

    def scan(self, document):
        raise NotImplemented


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionPrinter(Machine):
    def print(self, document):
        pass  # OK

    def fax(self, document):
        pass  # noop

    def scan(self, document):
        """Not supported."""
        raise NotImplemented('Printer cannot scan.')


"""
ISP 
"""


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class Fax(ABC):
    def fax(self, document):
        pass


class MyPrinter(Printer):

    def print(self, document):
        pass


class Photocopier(Printer, Scanner):

    def print(self, document):
        pass

    def scan(self, document):
        pass


class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer: Printer, scaner: Scanner):
        self.scaner = scaner
        self.printer = printer

    def print(self, document):
        pass

    def scan(self, document):
        pass
