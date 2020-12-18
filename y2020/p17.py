import sys
from itertools import product


def span(n):
    return list(range(-n - 1, n + 2))


def neighbors(pos):
    return {
        tuple(t + dt for t, dt in zip(pos, deltas))
        for deltas in product([-1, 0, 1], repeat=len(pos))
        if set(deltas) != {0}
    }


def condition(known, pos):
    active = pos in known
    count = len(neighbors(pos) & known)
    return (active and count in {2, 3}) or (not active and count in {3})


def evolve(known, dims, n_cycles):
    for _ in range(n_cycles):
        dims = [n + 1 for n in dims]
        known = {
            pos
            for pos in product(*map(span, dims))
            if condition(known, pos)
        }
    return known


text = sys.stdin.read()
known = {
    (x, y, 0)
    for y, ln in enumerate(text.splitlines())
    for x, char in enumerate(ln)
    if char == '#'
}
dims = tuple([
    max(x + 1 for x, _, _ in known),
    max(y + 1 for _, y, _ in known),
    max(z + 1 for _, _, z in known),
])
print(len(evolve(known, dims, 6)))
print(len(evolve({pt + (0,) for pt in known}, dims + (1,), 6)))
