# Filename      :       001_intrusive_visitor.py
# Created By    :       Suyog Shimpi
# Created Date  :       27/05/22

class DoubleExpression:  # noqa
    def __init__(self, value):
        self.value = value

    def print(self, buffer: list) -> None:  # noqa
        buffer.append(str(self.value))

    def eval(self) -> int:  # noqa
        return self.value


class AdditionExpression:  # noqa
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def print(self, buffer: list) -> None:  # noqa
        buffer.append('(')
        self.left.print(buffer)
        buffer.append(' + ')
        self.right.print(buffer)
        buffer.append(')')

    def eval(self) -> int:  # noqa
        return self.left.eval() + self.right.eval()


if __name__ == '__main__':
    # 1 + (2 + 3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )

    _buffer = []
    e.print(_buffer)
    print(''.join(_buffer), '=', e.eval())
