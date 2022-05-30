# Filename      :       003_switch_based_state_machine.py
# Created By    :       Suyog Shimpi
# Created Date  :       26/05/22
from enum import Enum, auto


class State(Enum):  # noqa
    LOCKED = auto()  # noqa
    FAILED = auto()  # noqa
    UNLOCKED = auto()  # noqa


if __name__ == '__main__':
    code = '1234'
    state = State.LOCKED
    entry = ''

    while True:
        if state == State.LOCKED:
            entry += input(entry)

            if entry == code:
                state = State.UNLOCKED

            if not code.startswith(entry):
                state = State.FAILED
        elif state == State.FAILED:
            print('\nFAILED')
            entry = ''
            state = State.LOCKED
        elif state == State.UNLOCKED:
            print('\nUNLOCKED')
            break
