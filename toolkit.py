import builtins
import collections
import functools
import hashlib
import importlib
import itertools
import math
import operator
import os
import re
import string
import sys
from pathlib import Path


product = functools.partial(functools.reduce, operator.mul)


def render(grid, brush=None):
    if brush is None:
        brush = {v: v for v in grid.values()}
    if isinstance(brush, str):
        brush = {i: c for i, c in enumerate(brush)}
    xmin, *_, xmax = sorted(int(p.real) for p in grid)
    ymin, *_, ymax = sorted(int(p.imag) for p in grid)
    brush[None] = ' '
    rendered = ''
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            rendered += brush[grid.get(complex(x, y))]
        rendered += '\n'
    return rendered


def read_image(text):
    grid = collections.defaultdict(str)
    for y, line in enumerate(text.splitlines()):
        for x, cell in enumerate(line):
            grid[complex(x, y)] = cell
    return grid, x + 1, y + 1


def shortest_path(start, end, move):
    seen = {}
    edge = {start: None}
    while edge:
        seen.update(edge)
        edge = {
            adj: pos
            for pos in edge
            for adj in move(pos)
            if adj not in seen
        }
        if end in seen:
            break
    else:
        raise RuntimeError('Path not found', seen)
    path = []
    while end:
        path.append(end)
        end = seen[end]
    return path[::-1]


def batch(iterable, size):
    count = itertools.count()
    for _, sub in itertools.groupby(iterable, lambda _: next(count) // size):
        yield sub


def md5(string):
    return hashlib.md5(string.encode()).hexdigest()


def loop_consume(lines, handler):
    instructions = collections.deque(lines)
    count = 0
    while instructions:
        ok = handler(instructions[0])
        if ok:
            instructions.popleft()
            count = 0
        elif count < len(instructions):
            instructions.rotate(1)
            count += 1
        else:
            raise RuntimeError('Reached steady state')
