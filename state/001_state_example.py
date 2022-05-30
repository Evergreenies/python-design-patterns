# Filename      :       001_state_example.py
# Created By    :       Suyog Shimpi
# Created Date  :       26/05/22
from abc import ABC


class State(ABC):  # noqa
    def on(self, switch) -> None:  # noqa
        print('Light is already on.')

    def off(self, switch) -> None:  # noqa
        print('Light is already off.')


class OnState(State):  # noqa
    def __init__(self):
        print('Light is turned on.')

    def off(self, switch) -> None:  # noqa
        print('Turning light off...')
        switch.state = OffState()


class OffState(State):  # noqa
    def __init__(self):
        print('Light turned off.')

    def on(self, switch):  # noqa
        print('Turning light on...')
        switch.state = OnState()


class Switch:  # noqa
    def __init__(self):
        self.state = OffState()

    def on(self):  # noqa
        self.state.on(self)

    def off(self):  # noqa
        self.state.off(self)


if __name__ == '__main__':
    sw = Switch()
    sw.on()
    sw.off()
    sw.off()
