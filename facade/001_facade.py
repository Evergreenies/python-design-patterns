# Filename      :       facade.py
# Created By    :       Suyog Shimpi
# Created Date  :       24/05/22


class Buffer:  # noqa
    def __init__(self, width: int = 30, height: int = 20):
        self.height = height
        self.width = width
        self._buffer = [' '] * (width * height)  # noqa

    def __getitem__(self, item: int):
        return self._buffer.__getitem__(item)

    def write(self, text: str):  # noqa
        self._buffer += text


class Viewport:  # noqa
    def __init__(self, buffer: Buffer = Buffer()):
        self._buffer = buffer
        self.offset = 0

    def get_char_at(self, index: int):  # noqa
        return self._buffer[index + self.offset]

    def append(self, text: str):  # noqa
        self._buffer.write(text)


class Console:  # noqa
    def __init__(self):
        b = Buffer()
        self.current_viewport = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    def write(self, text: str):  # noqa
        self.current_viewport._buffer.write(text)  # noqa

    def get_char_at(self, index: int):  # noqa
        return self.current_viewport.get_char_at(index)


if __name__ == '__main__':
    c = Console()
    c.write('Hello')
    print(c.get_char_at(-1))
