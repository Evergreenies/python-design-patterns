# Filename      :       002_phone_call.py
# Created By    :       Suyog Shimpi
# Created Date  :       26/05/22
from enum import Enum, auto


class State(Enum):  # noqa
    OFF_HOOK = auto()  # noqa
    CONNECTING = auto()  # noqa
    CONNECTED = auto()  # noqa
    ON_HOLD = auto()  # noqa
    ON_HOOK = auto()  # noqa


class Trigger(Enum):  # noqa
    CALL_DIALED = auto()  # noqa
    HUNG_UP = auto()  # noqa
    CALL_CONNECTED = auto()  # noqa
    PLACED_ON_HOLD = auto()  # noqa
    TAKEN_OFF_HOLD = auto()  # noqa
    LEFT_MESSAGE = auto()  # noqa


if __name__ == '__main__':
    _rules = {
        State.OFF_HOOK: [
            (Trigger.CALL_DIALED, State.CONNECTING)
        ],
        State.CONNECTING: [
            (Trigger.HUNG_UP, State.ON_HOOK),
            (Trigger.CALL_CONNECTED, State.CONNECTED)
        ],
        State.CONNECTED: [
            (Trigger.LEFT_MESSAGE, State.ON_HOOK),
            (Trigger.HUNG_UP, State.ON_HOOK),
            (Trigger.PLACED_ON_HOLD, State.ON_HOLD)
        ],
        State.ON_HOLD: [
            (Trigger.TAKEN_OFF_HOLD, State.CONNECTED),
            (Trigger.HUNG_UP, State.ON_HOOK)
        ]
    }

    state = State.OFF_HOOK
    exit_state = State.ON_HOOK

    while state != exit_state:
        print(f'The phone is currently {state}')

        for index in range(len(_rules[state])):
            tup = _rules[state][index][0]
            print(f'{index}: {tup}')

        idx = int(input('Select trigger: '))
        s = _rules[state][idx][1]
        state = s
    print('We are done using the phone.')
