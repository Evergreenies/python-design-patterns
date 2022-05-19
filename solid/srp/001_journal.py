# Filename      :       001_journal.py
# Created By    :       Suyog Shimpi
# Created Date  :       18/05/22

class Journal(object):
    """A journal"""

    def __init__(self):
        self.entries = []
        self.count = 0

    def make_entry(self, text: str) -> None:
        """Make entry in journal"""
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, position: int) -> None:
        """Remove entry from journal"""
        del self.entries[position]

    def __str__(self) -> str:
        return '\n'.join(self.entries)


class PersistenceManager:
    """Persistence Manager"""

    @staticmethod
    def save_to_file(journal: Journal, filename: str) -> None:
        """Save journal to file"""
        with open(filename, 'w') as fp:
            fp.write(str(journal))

    def load_from_file(self, filename: str) -> None:  # noqa
        pass

    def load_from_web(self, url: str) -> None:  # noqa
        pass


if __name__ == '__main__':
    _journal = Journal()
    _journal.make_entry('I cried today.')
    _journal.make_entry('I ate a mange.')
    print(f'Journal entries: \n{_journal}')
    PersistenceManager.save_to_file(_journal, 'temp_file.txt')

    # Print text saved in file
    with open('temp_file.txt') as fp:
        print(fp.read())
