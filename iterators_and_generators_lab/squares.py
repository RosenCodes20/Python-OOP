def squares(n):
    idx = 1

    while idx <= n:
        yield idx ** 2
        idx += 1


print(list(squares(5)))