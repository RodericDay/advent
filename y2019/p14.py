import collections
import math
import re
import sys


text = sys.stdin.read()
to_get = {}
for line in text.strip().splitlines():
    for i, (qty, name) in enumerate(re.findall(r'(\d+) ([A-Z]+)', line)[::-1]):
        if i == 0:
            output = name
            to_get[output] = {output: -int(qty)}
        else:
            to_get[output][name] = int(qty)


def fuel_to_ore(wanted):
    required = collections.Counter({'FUEL': wanted})
    pending = required.copy()
    while pending:
        pending = {k: v for k, v in required.items() if k != 'ORE' and v > 0}
        for out, out_qty in pending.items():
            min_qty = -to_get[out][out]
            n_times = math.ceil(out_qty / min_qty)
            required.update({k: v * n_times for k, v in to_get[out].items()})
    return required['ORE']


print(fuel_to_ore(1))


def bsearch(fn, goal, lo, hi):
    while hi - lo > 1:
        mid = lo + (hi - lo) // 2
        if goal < fn(mid):
            lo, hi = lo, mid
        else:
            lo, hi = mid, hi

    # check
    a, b = fn(lo), fn(hi)
    assert a <= goal, 'lower bound too high'
    assert goal <= b, 'higher bound too low'

    return lo


print(bsearch(fuel_to_ore, 1E12, 1, 10_000_000))
