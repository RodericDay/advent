import sys
import itertools
from intcode import compute


ns = sys.stdin.read()


def solve(ns, phases):
    out = 0
    for n in phases:
        out = list(compute(ns, iter([n, out])))[-1]
    return out

print(max(solve(ns, phases) for phases in itertools.permutations(range(5))))


def solve2(ns, phases):
    feedback = []
    iter_phases = iter(phases)
    iter_feed = iter(feedback)
    loop = itertools.cycle([
        compute(ns, itertools.chain([next(iter_phases), 0], iter_feed)),
        compute(ns, itertools.chain([next(iter_phases)], iter_feed)),
        compute(ns, itertools.chain([next(iter_phases)], iter_feed)),
        compute(ns, itertools.chain([next(iter_phases)], iter_feed)),
        compute(ns, itertools.chain([next(iter_phases)], iter_feed)),
    ])
    try:
        for machine in loop:
            feedback.append(next(machine))
    except StopIteration:
        return feedback[-1]

print(max(solve2(ns, phases) for phases in itertools.permutations(range(5, 10))))
