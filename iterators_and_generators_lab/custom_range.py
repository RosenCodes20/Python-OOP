class custom_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.index = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index <= self.end:
            return self.index

        raise StopIteration


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
