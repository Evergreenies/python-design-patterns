# Filename      :       001_memento.py
# Created By    :       Suyog Shimpi
# Created Date  :       26/05/22


class Memento:  # noqa
    def __init__(self, balance: int):
        self.balance = balance


class BankAccount:  # noqa
    def __init__(self, balance: int = 0):
        self.balance = balance
        self.changes = [Memento(self.balance)]
        self.current = 0

    def deposit(self, amount: int):  # noqa
        prev_bal = self.balance
        self.balance += amount
        print(f'Deposited amount {amount} to your account. Your previous balance '
              f'was {prev_bal}, and latest balance is {self.balance}')
        m = Memento(self.balance)
        self.changes.append(m)
        self.current += 1
        return m

    def restore(self, memento: Memento):  # noqa
        if memento:
            self.balance = memento.balance
            self.changes.append(memento)
            self.current = len(self.changes) - 1

    def undo(self):  # noqa
        if self.current > 0:
            self.current -= 1
            m = self.changes[self.current]
            self.balance = m.balance
            return m
        return None

    def redo(self):  # noqa
        if self.current + 1 < len(self.changes):
            self.current += 1
            m = self.changes[self.current]
            self.balance = m.balance
            return m
        return None

    def __str__(self):
        return f'Balance = {self.balance}'


if __name__ == '__main__':
    _account = BankAccount(100)
    _account.deposit(50)
    _account.deposit(25)
    print(_account)

    _account.undo()
    print(f'Undo 1: {_account}')
    _account.undo()
    print(f'Undo 2: {_account}')
    _account.redo()
    print(f'Redo 1: {_account}')
