def fibonacci():
    x1, x2 = 0, 1

    while True:
        yield x1
        x1, x2 = x2, x1 + x2
        

generator = fibonacci()
for i in range(5):
    print(next(generator))

