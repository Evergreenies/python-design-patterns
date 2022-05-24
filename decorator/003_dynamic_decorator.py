# Filename      :       dynamic_decorator.py
# Created By    :       Suyog Shimpi
# Created Date  :       24/05/22


class FileWithLogging:  # noqa
    def __init__(self, file):
        self.file = file

    def writelines(self, strings):  # noqa
        self.file.writelines(strings)
        print(f'Wrote {len(strings)} lines')

    def write(self, item):  # noqa
        self.file.write(item)

    def __iter__(self):
        return self.file.__iter__()

    def __next__(self):
        return self.file.__next__()

    def __getattr__(self, item):
        return getattr(self.__dict__['file'], item)

    def __setattr__(self, key, value):
        if key == 'file':
            self.__dict__[key] = value
        else:
            setattr(self.__dict__['file'], key, value)

    def __delattr__(self, item):
        delattr(self.__dict__['file'], item)


if __name__ == '__main__':
    _file = FileWithLogging(open('hello.txt', 'w'))
    _file.writelines(['Hello', 'world'])
    _file.write('testing')
    _file.close()
