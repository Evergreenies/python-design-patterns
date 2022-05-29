# Filename      :       001_user_names.py
# Created By    :       Suyog Shimpi
# Created Date  :       25/05/22
import random
import string


class User:  # noqa
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'{self.name}'


class User2:  # noqa
    strings = []

    def __init__(self, full_name: str):
        def get_or_add(s):  # noqa
            if s in self.strings:
                return self.strings.index(s)
            self.strings.append(s)
            return len(self.strings) - 1

        self.names = [get_or_add(x) for x in full_name.split(' ')]

    def __str__(self):
        return ' '.join([self.strings[x] for x in self.names])


def random_string() -> str:  # noqa
    chars = string.ascii_lowercase
    return ''.join(
        [random.choice(chars) for _ in range(8)]
    )


if __name__ == '__main__':
    users = []
    first_name = [random_string() for _ in range(100)]
    last_name = [random_string() for _ in range(100)]

    for first in first_name:
        for last in last_name:
            users.append(User2(f'{first} {last}'))

    print(users[0])
