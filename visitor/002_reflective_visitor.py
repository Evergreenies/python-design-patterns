# Filename      :       002_reflective_visitor.py
# Created By    :       Suyog Shimpi
# Created Date  :       27/05/22
from abc import ABC


class Expression(ABC):  # noqa
    pass


class DoubleExpression(Expression):  # noqa
    def __init__(self, value):
        self.value = value


class AdditionExpression(Expression):  # noqa
    def __init__(self, left, right):
        self.left = left
        self.right = right


class ExpressionPrinter:  # noqa
    @staticmethod
    def print(e_, buffer: list) -> None:  # noqa
        if isinstance(e_, DoubleExpression):
            buffer.append(str(e_.value))
        elif isinstance(e_, AdditionExpression):
            buffer.append('(')
            ExpressionPrinter.print(e_.left, buffer)
            buffer.append(' + ')
            ExpressionPrinter.print(e_.right, buffer)
            buffer.append(')')

    Expression.print = lambda self, b: ExpressionPrinter.print(self, b)


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
    e.print(_buffer)  # noqa
    # ExpressionPrinter.print(e, _buffer)
    print(''.join(_buffer))  # , '=', e.eval())
