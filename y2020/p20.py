# flake8: noqa
import re
import collections
import itertools
import sys
import math

import toolkit


def apply(cell):
    key, *fns = cell
    string = tiles[key]
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
        for ln in zip(*[apply(cell).splitlines()[1:-1] for cell in row]))
        for row in grid
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


text = sys.stdin.read().strip()
tiles = {}
borders = {}
for line in text.split('\n\n'):
    title, content = line.split(':\n')
    tid = int(title.split()[1])
    tiles[tid] = content
    borders[tid] = get_borders(content)


size = int(len(borders) ** 0.5)


adj = collections.defaultdict(set)
for (aid, A), (bid, B) in itertools.combinations(borders.items(), 2):
    if set(A) & set(B):
        adj[aid].add(bid)
        adj[bid].add(aid)

corn = [v for v, ks in adj.items() if len(ks) == 2]

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


grid = [[(gids[y][x],) for x in range(size)] for y in range(size)]
grid[0][0] += (flipV,)

options = list(itertools.product([None, flipH], [None, flipV], [None] + [rot90(n) for n in range(3)]))

for x in range(1, size):
    goal = [ln[-1] for ln in apply(grid[0][x - 1]).splitlines()]
    for chain in options:
        if goal == [ln[0] for ln in apply(grid[0][x] + chain).splitlines()]:
            grid[0][x] += chain
            break

for y in range(1, size):
    for x in range(size):
        goal = apply(grid[y - 1][x]).splitlines()[-1]
        for chain in options:
            if goal == apply(grid[y][x] + chain).splitlines()[0]:
                grid[y][x] += chain
                break


monster = '''                  #
#    ##    ##    ###
 #  #  #  #  #  #   '''
kuk, W, H = toolkit.read_image(monster)
goal = re.compile(toolkit.render(kuk).replace('\n', '').replace(' ', '.'))

cnt = 0
for chain in options:
    grody = apply2(render(grid), chain)
    grok = [list(line) for line in grody.splitlines()]
    for y in range(len(grok) - H):
        for x in range(len(grok[0]) - W):
            sample = ''.join(''.join(grok[y + dy][x + dx] for dx in range(W)) for dy in range(H))
            cnt += bool(goal.fullmatch(sample))
    if cnt:
        break

print(grody)
print(grody.count('#') - cnt * monster.count('#'))
