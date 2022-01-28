from itertools import cycle

iterator = cycle([1, 2, 3, 4])

for _ in range(10):
    print(next(iterator))
