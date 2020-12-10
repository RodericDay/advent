import collections
import itertools
import sys


def recurse(n, sources, cache={0: 1}):
    if n not in cache:
        cache[n] = sum(recurse(m, sources) for m in sources[n])
    return cache[n]


text = sys.stdin.read()

ns = [int(n) for n in text.splitlines()]
ns += [0, max(ns) + 3]
ns.sort()

a, b = collections.Counter([b - a for a, b in zip(ns, ns[1:])]).values()
print(a * b)

sources = collections.defaultdict(list)
for a, b in itertools.combinations(ns, 2):
    if b - a <= 3:
        sources[b].append(a)
print(recurse(ns[-1], sources))
