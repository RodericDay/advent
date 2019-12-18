import sys

from intcode import compute


def check(x, y):
    return next(compute(text, iter([x, y])))


text = sys.stdin.read()
tiles = {(x, y) for x in range(50) for y in range(50) if check(x, y)}
print(len(tiles))

x, y = 0, 0
while not check(x + 99, y):
    y += 1
    while not check(x, y + 99):
        x += 1
print(x * 10_000 + y)
