# Filename      :       002_text_formatting.py
# Created By    :       Suyog Shimpi
# Created Date  :       25/05/22

class FormattedText:  # noqa
    def __init__(self, plain_text: str):
        self.plain_text = plain_text
        self.caps = [False] * len(plain_text)

    def capitalize(self, start: int, end: int):  # noqa
        for index in range(start, end):
            self.caps[index] = True

    def __str__(self):
        result = []
        for index in range(len(self.plain_text)):
            c = self.plain_text[index]
            result.append(
                c.upper() if self.caps[index] else c
            )
        return ''.join(result)


class BetterFormattedText:  # noqa
    def __init__(self, plain_text: str):
        self.plain_text = plain_text
        self.formatting = []

    class TextRange:  # noqa
        def __init__(self, start: int, end: int, capitalize: bool = False):
            self.start = start
            self.end = end
            self.capitalize = capitalize

        def covers(self, position: int) -> bool:  # noqa
            return self.start <= position <= self.end

    def get_range(self, start: int, end: int) -> TextRange:  # noqa
        _range = self.TextRange(start, end)
        self.formatting.append(_range)
        return _range

    def __str__(self):
        result = []
        for index in range(len(self.plain_text)):
            c = self.plain_text[index]

            for r in self.formatting:
                if r.covers(index) and r.capitalize:
                    c = c.upper()
            result.append(c)
        return ''.join(result)


if __name__ == '__main__':
    text = 'This is a brave new world'
    ft = FormattedText(text)
    ft.capitalize(10, 15)
    print(ft)
    print()

    bft = BetterFormattedText(text)
    bft.get_range(16, 19).capitalize = True
    print(bft)
