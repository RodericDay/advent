import sys
from functools import lru_cache

from toolkit import read_image


def simple_adjace(level, pos):
    inbound = {pos + ori for ori in [1, -1, 1j, -1j]} & domain
    return [(level, p) for p in inbound]


@lru_cache(maxsize=None)
def recursive_adjace(level, pos, center=complex(2, 2)):
    neis = []
    for ori in [1, -1, 1j, -1j]:
        adj = pos + ori
        if adj == center:
            neis += [(level + 1, p) for p in domain if p - ori not in domain]
        elif adj not in domain:
            neis += [(level - 1, center + ori)]
        else:
            neis += [(level, adj)]
    return neis


def evolve(bugs, adjacency, lim=None):
    seen_states = set()
    while lim is None or len(seen_states) < lim:
        affected = {nei for tile in bugs for nei in adjacency(*tile)} | bugs
        infested = set()
        dead = set()

        for tile in affected:
            count = sum(nei in bugs for nei in adjacency(*tile))
            if tile in bugs and count != 1:
                dead.add(tile)
            elif tile not in bugs and count in [1, 2]:
                infested.add(tile)

        bugs = bugs - dead | infested
        if bugs in seen_states:
            break
        seen_states.add(bugs)
    return bugs


text = sys.stdin.read()
domain = set(read_image(text))
bugs = frozenset((0, pos) for pos, c in read_image(text).items() if c == '#')

final = evolve(bugs, simple_adjace)
print(int(sum(2 ** (p.real + p.imag * 5) for _, p in final)))

final = evolve(bugs, recursive_adjace, 200)
print(len(final))
