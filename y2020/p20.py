import collections
import functools
import itertools
import math
import re
import sys


def render(grid):
    lines = []
    for y in range(size):
        groups = [tiles[grid[y, x]].splitlines()[1:-1] for x in range(size)]
        for lns in zip(*groups):
            lines.append(''.join(ln[1:-1] for ln in lns))
    return '\n'.join(lines)


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


def rot90(string):
    return flipH(transpose(string))


def noop(string):
    return string


def variants(string):
    alts = [noop, flipH], [noop, flipV], [noop, transpose]
    for ops in itertools.product(*alts):
        yield functools.reduce(lambda s, f: f(s), ops, string)


def UD(A, B):
    return A.splitlines()[-1] == B.splitlines()[0]


def LR(A, B):
    return UD(rot90(A), rot90(B))


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


def reconcile(A, B, condition):
    tiles[A], tiles[B] = next(
        (X, Y)
        for X, Y in itertools.product(variants(tiles[A]), variants(tiles[B]))
        if condition(X, Y)
    )


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
corners = [v for v, ks in adj.items() if len(ks) == 2]
print(math.prod(corners))


A = min(corners)
B, C = adj.pop(A)

grid = {(y, x): None for x in range(size) for y in range(size)}
grid[0, 0] = A
grid[0, 1] = B
grid[1, 0] = C
reconcile(A, B, condition=LR)
reconcile(A, C, condition=UD)

seen = {A, B, C}
for z in range(2, 2 * size - 1):
    # determine new pieces from intersection between 2 neighbors
    for y, x in {(y, z - y) for y in range(1, z)}.intersection(grid):
        U, L = (y - 1, x), (y, x - 1)
        grid[y, x], = adj[grid[U]] & adj[grid[L]] - seen
        reconcile(grid[L], grid[y, x], condition=LR)
        seen.add(grid[y, x])

    # determine new piece from only one alternative left
    for y, x in {(0, z), (z, 0)}.intersection(grid):
        opts = {(y - 1, x): UD, (y, x - 1): LR}
        P, fn = next(p for p in opts.items() if p[0] in grid)
        grid[y, x], = adj[grid[P]] - seen
        reconcile(grid[P], grid[y, x], condition=fn)
        seen.add(grid[y, x])

monster = '''
..................#.
#....##....##....###
.#..#..#..#..#..#...
'''[1:-1]
src = render(grid)
found = max([search_in(pic, monster) for pic in variants(src)], key=len)
print(src.count('#') - len(found) * monster.count('#'))
