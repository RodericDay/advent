# flake8: noqa
import re
import collections
import itertools
import sys
import math
from functools import reduce


def render(grid):
    return '\n'.join(
        '\n'.join(''.join([n[1:-1]
            for n in ln])
        for ln in zip(*[grid[y, x].splitlines()[1:-1] for x in range(size)]))
        for y in range(size)
    )


def get_borders(content):
    a, *_, b = content.splitlines()
    c, *_, d = [''.join(ln) for ln in zip(*content.splitlines())]
    return [a, b, c, d, a[::-1], b[::-1], c[::-1], d[::-1]]


def transpose(string):
    return '\n'.join(''.join(ln) for ln in zip(*string.splitlines()))


def flipV(string):
    return '\n'.join(ln for ln in string.splitlines()[::-1])


def flipH(string):
    return '\n'.join(ln[::-1] for ln in string.splitlines())


def rot90(n):
    def inner(string):
        return flipH(transpose(string))
    return inner


def noop(string):
    return string


def variants(string):
    alts = [noop, flipH], [noop, flipV], [noop, rot90(1), rot90(2), rot90(3)]
    for ops in itertools.product(*alts):
        yield reduce(lambda s, f: f(s), ops, string)


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


grid = {(y, x): tiles[gids[y][x]] for x in range(size) for y in range(size)}


def UD(A, B):
    return A.splitlines()[-1] == B.splitlines()[0]

def LR(A, B):
    return UD(rot90(1)(A), rot90(1)(B))


for y in range(size):
    for x in range(size):
        if (y, x) == (0, 0):
            grid[y, x] = flipV(grid[y, x])
        elif y == 0:
            grid[y, x] = next(pic for pic in variants(grid[0, x]) if LR(grid[y, x - 1], pic))
        else:
            grid[y, x] = next(pic for pic in variants(grid[y, x]) if UD(grid[y - 1, x], pic))


monster = '''
..................#.
#....##....##....###
.#..#..#..#..#..#...
'''[1:-1]
src = render(grid)
found = max([search_in(pic, monster) for pic in variants(src)], key=len)
print(src.count('#') - len(found) * monster.count('#'))
