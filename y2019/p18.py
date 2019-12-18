import collections
import itertools
import sys

from toolkit import read_image, render


def read_in(text):
    grid = read_image(text)
    elements = {v: k for k, v in grid.items()}
    keys = frozenset(k for k in elements if 'a' <= k <= 'z')
    return dict(grid), elements, keys


def move(pos):
    for ori in [1, -1, 1j, -1j]:
        if grid[pos + ori] != '#':
            yield pos + ori


def shortest_path(start, end, move):
    seen = {}
    edge = {start: None}
    while end not in seen:
        edge = {
            adj: pos
            for pos in edge
            for adj in move(pos)
            if adj not in seen
        }
        seen.update(edge)
        if not edge:
            raise RuntimeError('No path found')
    path = []
    while end != start:
        path.append(end)
        end = seen[end]
    return path


def trim(states):
    groups = collections.defaultdict(list)
    for state in states:
        tips = frozenset(seq[-1] for seq in state)
        bulk = frozenset(' '.join(state))
        groups[bulk, tips].append(state)
    return [min(groups[k], key=calc_total) for k in groups]


def precalc_moves(entrances):
    requirements = collections.defaultdict(dict)
    lengths = collections.defaultdict(dict)
    for a, b in itertools.permutations(keys.union(entrances), 2):
        try:
            path = shortest_path(elements[a], elements[b], move)
        except RuntimeError:
            continue
        lengths[a][b] = len(path)
        requirements[a][b] = {
            e.lower()
            for e, v in elements.items()
            if e.isupper()
            and v in path
        }
    return requirements, lengths


def calc_total(state):
    return sum(sum(
        lengths[a][b]
        for a, b in zip(s, s[1:])
        if {a, b} < set(lengths)
    ) for s in state)


def mod_grid(text):
    grid, elements, keys = read_in(text)
    pos = elements['@']
    grid[pos] = '#'
    for char, ori in zip('*&^@', [1, -1, 1j, -1j]):
        grid[pos + ori] = '#'
        grid[pos + ori + ori * 1j] = char
    return render(grid, {k: k for k in grid.values()})


def solve(text):
    global grid, elements, keys, lengths
    grid, elements, keys = read_in(text)
    stacks = {k for k in elements if not k.isalnum()} - {'#', '.'}
    requirements, lengths = precalc_moves(stacks)
    states = [stacks]
    for _ in range(len(keys)):
        states = trim(
            state - {seq} | {seq + b}
            for state in states
            for seq in state
            for b, reqs in requirements[seq[-1]].items()
            if b not in seq and reqs.issubset(''.join(state))
        )
    final = min(states, key=calc_total)
    print(' '.join(sorted(final)))
    print(calc_total(final))


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
