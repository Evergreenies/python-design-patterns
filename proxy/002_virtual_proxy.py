# Filename      :       002_virtual_proxy.py
# Created By    :       Suyog Shimpi
# Created Date  :       25/05/22

"""
Virtual Proxy:- Appears to be the fully initialized object.
"""


class Bitmap:  # noqa
    def __init__(self, filename: str):
        self.filename = filename
        print(f'Loading image from {self.filename}')

    def draw(self):  # noqa
        print(f'Drawing image {self.filename}')


class LazyBitmap:  # noqa
    def __init__(self, filename: str):
        self.filename = filename
        self._bitmap = None

    def draw(self):  # noqa
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()


def draw_image(image):  # noqa
    print('About to draw image')
    image.draw()
    print('Done')


if __name__ == '__main__':
    bmp = LazyBitmap('facepalm.jpeg')
    draw_image(bmp)
    draw_image(bmp)
