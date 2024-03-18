def genrange(start, end):
    idx = start

    while idx <= end:
        yield idx
        idx += 1


print(list(genrange(1, 10)))