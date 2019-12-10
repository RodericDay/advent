import itertools
import math
import sys
from functools import partial


def measure(start, other):
    dx, dy = other[0] - start[0], other[1] - start[1]
    angle = math.atan2(-dx, dy)
    return -math.pi if angle == math.pi else angle, math.hypot(dx, dy), other


def seek(start, asteroids):
    pending = sorted(measure(start, ast) for ast in asteroids)
    while pending:
        copy = pending.copy()
        pending = []
        out = {}
        for angle, dist, ast in copy:
            if angle in out:
                pending.append((angle, dist, ast))
            else:
                out[angle] = ast
        yield list(out.values())


text = sys.stdin.read()
asteroids = {
    (X, Y)
    for Y, line in enumerate(text.splitlines())
    for X, cell in enumerate(line)
    if cell == '#'
}

visibility = {ast: len(next(seek(ast, asteroids))) for ast in asteroids}
origin = max(visibility, key=visibility.get)
print(visibility[origin])

ordering = list(itertools.chain(*seek(origin, asteroids)))
x, y = ordering[200 - 1]
print(100 * x + y)
