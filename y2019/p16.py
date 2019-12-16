import sys
from itertools import accumulate, cycle
from multiprocessing import Pool


def _next(ns, i):
    g = cycle([n for n in [0, 1, 0, -1] for _ in range(i + 1)])
    next(g)  # throw away one
    return abs(sum(a * b for a, b in zip(ns, g))) % 10


text = sys.stdin.read().strip()

ns = [int(n) for n in text]
with Pool() as pool:
    for _ in range(100):
        ns = pool.starmap(_next, [(ns, i) for i in range(len(ns))])
print(''.join(str(c) for c in ns[:8]))

offset = int(text[:7])
pending = [int(n) for n in (text * 10000)[offset:]][::-1]
for _ in range(100):
    pending = [n % 10 for n in accumulate(pending)]
print(''.join(str(c) for c in pending[::-1][:8]))
