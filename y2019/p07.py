import sys
from itertools import chain, cycle, permutations

from intcode import compute


ns = sys.stdin.read()


def solve(ns, phases):
    out = 0
    for n in phases:
        out = list(compute(ns, iter([n, out])))[-1]
    return out


print(max(solve(ns, phases) for phases in permutations(range(5))))


def solve2(ns, phases):
    feedback = []
    iter_phases = iter(phases)
    iter_feed = iter(feedback)
    loop = cycle([
        compute(ns, chain([next(iter_phases), 0], iter_feed)),
        compute(ns, chain([next(iter_phases)], iter_feed)),
        compute(ns, chain([next(iter_phases)], iter_feed)),
        compute(ns, chain([next(iter_phases)], iter_feed)),
        compute(ns, chain([next(iter_phases)], iter_feed)),
    ])
    try:
        for machine in loop:
            feedback.append(next(machine))
    except StopIteration:
        return feedback[-1]


print(max(solve2(ns, phases) for phases in permutations(range(5, 10))))
