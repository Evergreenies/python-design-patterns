# Filename      :       002_facade_example.py
# Created By    :       Suyog Shimpi
# Created Date  :       24/05/22


class Subsystem1:  # noqa
    """
    The sub-system can accept requests either from the facade or client directly. In
    any case, to the sub-system, the facade is yet another client, and it's not a part
    of the sub-system.
    """

    def operation1(self) -> str:  # noqa
        return 'Subsystem1: Ready!'

    def operation_n(self) -> str:  # noqa
        return 'Subsystem1: Go!'


class Subsystem2:  # noqa
    """
    Some facade can work with multiple sub-system at the same time.
    """

    def operation1(self) -> str:  # noqa
        return 'SubSystem2: Get ready!'

    def operation_z(self) -> str:  # noqa
        return 'Subsystem2: Fire!'


class Facade:  # noqa
    """
    The facade class provides a simple interface to the complex logic of one or sever
    sub-systems. The facade delegates the client requests to the appropriate objects
    within the sub-systems. The Facade is also responsible for managing their lifecycle.
    All of these shields the client from undesired complexity of the sub-systems.
    """

    def __init__(self, subsystem1: Subsystem1 = Subsystem1(), subsystem2: Subsystem2 = Subsystem2()):
        """
        Depending on your application's needs, you can provide the facade with existing
        subsystem objects or force the facade to create them on its own
        :param subsystem1:
        :type subsystem1:
        :param subsystem2:
        :type subsystem2:
        """
        self._subsystem1 = subsystem1
        self._subsystem2 = subsystem2

    def operation(self) -> str:  # noqa
        """
        The facade's methods are convenient shortcuts to the sophisticated functionality
        of th sub-systems. However, clients get only to a fraction of a sub-system's
        capabilities
        :return:
        :rtype:
        """
        result = [
            'Facade initializes sub-systems:',
            self._subsystem1.operation1(),
            self._subsystem2.operation1(),
            'Facade orders sub-systems to perform the action:',
            self._subsystem1.operation_n(),
            self._subsystem2.operation_z(),
        ]
        return '\n'.join(result)


def client_code(facade: Facade) -> None:  # noqa
    print(facade.operation())


if __name__ == '__main__':
    _subsystem1 = Subsystem1()
    _subsystem2 = Subsystem2()
    _facade = Facade(_subsystem1, _subsystem2)
    client_code(_facade)
