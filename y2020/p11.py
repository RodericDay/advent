import itertools
import sys

import toolkit


def is_taken(pos, state):
    taken = sum(pos + step in state for step in moves)
    if pos not in state and not taken:
        return True
    elif pos in state and taken >= 4:
        return False
    return pos in state


def is_taken2(pos, state):
    taken = 0
    for step in moves:
        for x in itertools.count(1):
            adj = (pos + step * x)
            if adj in seats or adj not in grid:
                taken += adj in state
                break
    if pos not in state and not taken:
        return True
    elif pos in state and taken >= 5:
        return False
    return pos in state


text = sys.stdin.read()
grid, _, _ = toolkit.read_image(text)
moves = {dx + dy for dx in [-1, 0, 1] for dy in [-1j, 0, 1j]} - {0}
seats = {pos for pos, value in grid.items() if value != '.'}

for fn in [is_taken, is_taken2]:
    state = frozenset()
    seen = set()
    while state not in seen:
        seen.add(state)
        state = frozenset({pos for pos in seats if fn(pos, state)})
    print(len(state))
