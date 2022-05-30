# Filename      :       lexing.py
# Created By    :       Suyog Shimpi
# Created Date  :       25/05/22
from enum import Enum, auto


class Token:  # noqa
    class Type(Enum):  # noqa
        INTEGER = auto()  # noqa
        PLUS = auto()  # noqa
        MINUS = auto()  # noqa
        LPAREN = auto()  # noqa
        RPAREN = auto()  # noqa

    def __init__(self, type_, text):
        self.type_ = type_
        self.text = text

    def __str__(self):
        return f'{self.text}'


def lex(inp) -> list:  # noqa
    result = []
    index = 0
    while index < len(inp):
        if inp[index] == '+':
            result.append(Token(Token.Type.PLUS, '+'))
        elif inp[index] == '-':
            result.append(Token(Token.Type.MINUS, '-'))
        elif inp[index] == '(':
            result.append(Token(Token.Type.LPAREN, '('))
        elif inp[index] == ')':
            result.append(Token(Token.Type.RPAREN, ')'))
        else:
            digits = [inp[index]]
            for j in range(index + 1, len(inp)):
                if inp[j].isdigit():
                    digits.append(inp[j])
                    index += 1
                else:
                    result.append(Token(Token.Type.INTEGER, ''.join(digits)))
                    break
        index += 1
    return result


class Integer:  # noqa
    def __init__(self, value):
        self.value = value


class BinaryExpression:  # noqa
    class Type(Enum):  # noqa
        ADDITION = auto()  # noqa
        SUBTRACTION = auto()  # noqa

    def __init__(self):
        self.type_ = None
        self.left = None
        self.right = None

    @property
    def value(self):  # noqa
        if self.type_ == self.Type.ADDITION:
            return self.left.value + self.right.value
        return self.left.value - self.right.value


def parse(tokens):  # noqa
    result = BinaryExpression()
    have_lhs = False
    index = 0
    while index < len(tokens):
        token = tokens[index]

        if token.type_ == Token.Type.INTEGER:
            integer = Integer(int(token.text))
            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer
        elif token.type_ == Token.Type.PLUS:
            result.type_ = BinaryExpression.Type.ADDITION
        elif token.type_ == Token.Type.MINUS:
            result.type_ = BinaryExpression.Type.SUBTRACTION
        elif token.type_ == Token.Type.LPAREN:
            j = index
            while j < len(tokens):
                if tokens[j].type_ == Token.Type.RPAREN:
                    break
                j += 1
            sub_expression = tokens[index + 1: j]
            element = parse(sub_expression)
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            index = j
        index += 1
    return result


def calc(inp: str):  # noqa
    tokens = lex(inp)
    print(' '.join(map(str, tokens)))

    parsed = parse(tokens)
    print(f'{inp} = {parsed.value}')


if __name__ == '__main__':
    calc('(13+4)-(12+1)')
