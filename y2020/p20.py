import functools
import itertools
import math
import re
import sys


def render(grid):
    lines = []
    for row in grid:
        for lns in zip(*[cell.splitlines()[1:-1] for cell in row]):
            lines.append(''.join(ln[1:-1] for ln in lns))
    return '\n'.join(lines)


class Ops:
    noop = lambda txt: txt  # noqa
    flipV = lambda txt: '\n'.join(ln for ln in txt.splitlines()[::-1])  # noqa
    flipH = lambda txt: '\n'.join(ln[::-1] for ln in txt.splitlines())  # noqa
    transpose = lambda txt: '\n'.join(map(''.join, zip(*txt.splitlines())))  # noqa


def variants(string):
    alts = [Ops.flipH, Ops.flipV, Ops.transpose]
    for ops in itertools.product(*[[Ops.noop, fn] for fn in alts]):
        yield functools.reduce(lambda s, f: f(s), ops, string)


def search_in(source, target):
    source_lns = source.splitlines()
    target_lns = target.splitlines()
    h, w = len(target_lns), len(target_lns[0])
    for y in range(len(source_lns)):
        for x in range(len(source_lns[0])):
            window = '\n'.join(ln[x:x + w] for ln in source_lns[y:y + h])
            if re.fullmatch(target, window):
                yield (x, y)


def find(old, new):
    delta = new - old
    base = fixed[old]

    if delta == -1: goal = [ln[0] for ln in base.splitlines()]  # noqa
    elif delta == 1: goal = [ln[-1] for ln in base.splitlines()]  # noqa
    elif delta == 1j: goal = base.splitlines()[-1]  # noqa
    elif delta == -1j: goal = base.splitlines()[0]  # noqa

    for tid, tile in tiles.items():
        for var in variants(tile):

            if delta == -1: found = [ln[-1] for ln in var.splitlines()]  # noqa
            elif delta == 1: found = [ln[0] for ln in var.splitlines()]  # noqa
            elif delta == 1j: found = var.splitlines()[0]  # noqa
            elif delta == -1j: found = var.splitlines()[-1]  # noqa

            if goal == found:
                tiles.pop(tid)
                grid[new] = tid
                fixed[new] = var
                yield tid
                return


text = sys.stdin.read().strip()
tiles = {}
for line in text.split('\n\n'):
    title, content = line.split(':\n')
    tid = int(title.split()[1])
    tiles[tid] = content
size = int(len(tiles) ** 0.5)

start = min(tiles, key=tiles.get)
fixed = {0: tiles.pop(start)}
grid = {0: start}
while tiles:
    grid.update({
        new: good
        for old in list(grid)
        for new in {old - 1, old + 1, old + 1j, old - 1j} - set(fixed)
        for good in find(old, new)
    })

xs = xmin, *_, xmax = sorted({int(p.real) for p in fixed})
ys = ymin, *_, ymax = sorted({int(p.imag) for p in fixed})
print(math.prod(grid[x + 1j * y] for x in [xmin, xmax] for y in [ymin, ymax]))

monster = '''
..................#.
#....##....##....###
.#..#..#..#..#..#...
'''[1:-1]
src = render([[fixed[complex(x, y)] for x in xs] for y in ys])
found = max([list(search_in(pic, monster)) for pic in variants(src)], key=len)
print(src.count('#') - len(found) * monster.count('#'))
