import collections
import math
import re
import sys

from toolkit import bsearch


text = sys.stdin.read()
cookbook = {}
for line in text.strip().splitlines():
    for i, (qty, name) in enumerate(re.findall(r'(\d+) ([A-Z]+)', line)[::-1]):
        if i == 0:
            output = name
            cookbook[output] = {output: -int(qty)}
        else:
            cookbook[output][name] = int(qty)


def fuel_to_ore(state):
    state = collections.Counter(state)
    pending = state.copy()
    while pending:
        pending = {k: v for k, v in state.items() if k in cookbook and v > 0}
        for out, out_qty in pending.items():
            min_qty = -cookbook[out][out]
            n_times = math.ceil(out_qty / min_qty)
            state.update({k: v * n_times for k, v in cookbook[out].items()})
    return state


print(fuel_to_ore({'FUEL': 1})['ORE'])
print(bsearch(lambda n: fuel_to_ore({'FUEL': n})['ORE'], 1E12, 1, 10_000_000))
