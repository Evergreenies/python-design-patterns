# Filename      :       001_template_example.py
# Created By    :       Suyog Shimpi
# Created Date  :       27/05/22
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    """
    The AbstractClass defines a template method that contains a skeleton of some
    algorithm, composed of calls to (usually) abstract primitive operations.
    Concrete subclass should implement these operations, but leave the template
    method itself intact.
    """

    def template_method(self) -> None:  # noqa
        """
        The template method defines the skeleton of an algorithm.
        :return:
        :rtype:
        """
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self) -> None:  # noqa
        print('AbstractClass says: I am doing the bulk of the work.')

    def base_operation2(self) -> None:  # noqa
        print('AbstractClass says: But, I let subclass override some operations.')

    def base_operation3(self) -> None:  # noqa
        print('AbstractClass says: But, I am doing bulk of work anyway.')

    @abstractmethod
    def required_operations1(self) -> None:  # noqa
        pass

    @abstractmethod
    def required_operations2(self) -> None:  # noqa
        pass

    def hook1(self) -> None:  # noqa
        pass

    def hook2(self) -> None:  # noqa
        pass


class ConcreteClass1(AbstractClass):
    """
    Concrete classes have to implement all abstract operations of the base class.
    They can also override some operation with default implementation.
    """

    def required_operations1(self) -> None:  # noqa
        print('ConcreteClass1 says: Implemented Operation1')

    def required_operations2(self) -> None:  # noqa
        print('ConcreteClass1 says: Implemented Operation2')


class ConcreteClass2(AbstractClass):
    """
    Usually, concrete classes override only a fraction of base class operations.
    """

    def required_operations2(self) -> None:  # noqa
        print('ConcreteClass2 says: Implemented Operation2')

    def required_operations1(self) -> None:  # noqa
        print('ConcreteClass2 says: Implemented Operation1')

    def hook1(self) -> None:  # noqa
        print('ConcreteClass@ says: Overridden hook1')


def client_code(abstract_class: AbstractClass) -> None:  # noqa
    abstract_class.template_method()


if __name__ == '__main__':
    print('Some client code can work with different subclasses:')
    client_code(ConcreteClass1())
    print()
    print('Some client code can work with different subclasses:')
    client_code(ConcreteClass2())
