class Reverse:
    def __init__(self, s: str):
        self.s = s
        self.length = len(s)  # 5

    def __iter__(self):
        return self

    def __next__(self):
        if not self.length:
            raise StopIteration
        self.length -= 1
        return self.s[self.length]


from typing import Union


class Cycle:
    def __iter__(self):
        return self

    def __init__(self, s: Union[str, list, set, tuple], count: int):
        self.index = -1
        self.s = s
        self.count = count
        self.length = len(s)  # noqa

    def __next__(self):
        self.index += 1
        if self.index == self.length:
            self.index = 0
            self.count -= 1
        if not self.count:
            raise StopIteration
        return self.s[self.index]  # noqa


def men_f():
    n = 0
    while n < 100:
        yield n
        n += 3
