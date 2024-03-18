class reverse_iter:

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index >= 0:
            return self.iterable[self.index]

        raise StopIteration


reversed_list = reverse_iter([4, 3, 2, 1])
for item in reversed_list:
    print(item)

