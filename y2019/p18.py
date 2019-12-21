import collections
import itertools
import sys
from functools import partial

from toolkit import read_image, render, shortest_path


def read_in(text):
    grid = read_image(text)
    elements = {v: k for k, v in grid.items()}
    keys = {c for c in elements if c.isalpha() and c.islower()}
    return dict(grid), elements, keys


def move(grid, pos):
    for ori in [1, -1, 1j, -1j]:
        if grid[pos + ori] != '#':
            yield pos + ori


def trim(states, metric):
    groups = collections.defaultdict(list)
    for state in states:
        tips = frozenset(seq[-1] for seq in state)
        bulk = frozenset(' '.join(state))
        groups[bulk, tips].append(state)
    return [min(groups[k], key=metric) for k in groups]


def precalc_moves(entrances, keys, elements, grid):
    requirements = collections.defaultdict(dict)
    lengths = {}
    for a, b in itertools.combinations(keys.union(entrances), 2):
        try:
            path = shortest_path(elements[a], elements[b], partial(move, grid))
            *glyphs, = map(grid.get, path)
        except RuntimeError:
            continue
        lengths[a, b] = len(path) - 1
        lengths[b, a] = len(path) - 1
        requirements[a][b] = {c.lower() for c in glyphs if c.isupper()}
        requirements[b][a] = {c.lower() for c in glyphs if c.isupper()}
    return requirements, partial(calc_total, lengths)


def calc_total(lengths, state):
    return sum(lengths[pair] for seq in state for pair in zip(seq, seq[1:]))


def mod_grid(text):
    grid, elements, keys = read_in(text)
    pos = elements['@']
    grid[pos] = '#'
    for char, ori in zip('*&^@', [1, -1, 1j, -1j]):
        grid[pos + ori] = '#'
        grid[pos + ori + ori * 1j] = char
    return render(grid)


def solve(text):
    grid, elements, keys = read_in(text)
    stacks = {k for k in elements if not k.isalnum()} - {'#', '.'}
    requirements, metric = precalc_moves(stacks, keys, elements, grid)
    states = [stacks]
    for _ in range(len(keys)):
        states = trim([
            state - {seq} | {seq + b}
            for state in states
            for seq in state
            for b, reqs in requirements[seq[-1]].items()
            if b not in seq and reqs.issubset(''.join(state))
        ], metric)
    best = min(states, key=metric)
    print(best)
    print(metric(best))


text = sys.stdin.read()
text = '''
#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba...BcIJ#
#####.@.#####
#nK.L...G...#
#M###N#H###.#
#o#m..#i#jk.#
#############
'''
solve(text)
text = mod_grid(text)
solve(text)
