# flake8: noqa
import re
import collections
import itertools
import sys
import math
from functools import reduce

import toolkit


def apply(cell):
    string, *fns = cell
    for fn in fns:
        if fn is not None:
            string = fn(string)
    return string


def apply2(string, fns):
    for fn in fns:
        if fn is not None:
            string = fn(string)
    return string


def render(grid):
    return '\n'.join(
        '\n'.join(''.join([n[1:-1]
            for n in ln])
        for ln in zip(*[apply(grid[y, x]).splitlines()[1:-1] for x in range(size)]))
        for y in range(size)
    )


def get_borders(content):
    a, *_, b = content.splitlines()
    c, *_, d = [''.join(ln) for ln in zip(*content.splitlines())]
    return [a, b, c, d, a[::-1], b[::-1], c[::-1], d[::-1]]


def flipV(string):
    return '\n'.join(ln for ln in string.splitlines()[::-1])


def flipH(string):
    return '\n'.join(ln[::-1] for ln in string.splitlines())


def rot90(n):
    def inner(string):
        return toolkit.render({k * 1j ** n: v for k, v in toolkit.read_image(string)[0].items()})
    return inner


def noop(string):
    return string


def variants(string):
    alts = [noop, flipH], [noop, flipV], [noop, rot90(1), rot90(2), rot90(3)]
    for ops in itertools.product(*alts):
        yield reduce(lambda s, f: f(s), ops, string), ops


def search_in(source, target):
    source_lns = source.splitlines()
    target_lns = target.splitlines()
    h, w = len(target_lns), len(target_lns[0])
    out = []
    for y in range(len(source_lns)):
        for x in range(len(source_lns[0])):
            window = '\n'.join(ln[x:x + w] for ln in source_lns[y:y + h])
            if re.fullmatch(target, window):
                out.append((x, y))
    return out


text = sys.stdin.read().strip()
tiles = {}
borders = {}
for line in text.split('\n\n'):
    title, content = line.split(':\n')
    tid = int(title.split()[1])
    tiles[tid] = content
    borders[tid] = get_borders(content)
size = int(len(tiles) ** 0.5)

adj = collections.defaultdict(set)
for (aid, A), (bid, B) in itertools.combinations(borders.items(), 2):
    if set(A) & set(B):
        adj[aid].add(bid)
        adj[bid].add(aid)
corn = [v for v, ks in adj.items() if len(ks) == 2]
print(math.prod(corn))


gids = [[None for _ in range(size)] for _ in range(size)]

gids[0][0] = corn[0]
gids[1][0], gids[0][1] = adj[gids[0][0]]
gids[1][1], = adj[gids[1][0]] & adj[gids[0][1]] - {gids[0][0]}

for x in range(2, size):
    gids[0][x], = adj[gids[0][x - 1]] - {gids[0][x - 2], gids[1][x - 1]}
    gids[1][x], = adj[gids[0][x]] & adj[gids[1][x - 1]] - {gids[0][x - 1]}

for y in range(2, size):
    gids[y][0], = adj[gids[y - 1][0]] - {gids[y - 2][0], gids[y - 1][1]}
    for x in range(1, size):
        gids[y][x], = adj[gids[y][x - 1]] & adj[gids[y - 1][x]] - {gids[y - 1][x - 1]}


options = list(itertools.product([None, flipH], [None, flipV], [None] + [rot90(n) for n in range(3)]))

grid = {(y, x): (tiles[gids[y][x]],) for x in range(size) for y in range(size)}
grid[0, 0] = (flipV(grid[0, 0][0]),)


for x in range(1, size):
    goal = [ln[-1] for ln in apply(grid[0, x - 1]).splitlines()]
    for chain in options:
        if goal == [ln[0] for ln in apply(grid[0, x] + chain).splitlines()]:
            grid[0, x] += chain
            break

for y in range(1, size):
    for x in range(size):
        goal = apply(grid[y - 1, x]).splitlines()[-1]
        for chain in options:
            if goal == apply(grid[y, x] + chain).splitlines()[0]:
                grid[y, x] += chain
                break


monster = '''
..................#.
#....##....##....###
.#..#..#..#..#..#...
'''[1:-1]
src = render(grid)
found = max([search_in(pic, monster) for pic, _ in variants(src)], key=len)
print(src.count('#') - len(found) * monster.count('#'))
