import math
import collections
import itertools
import re


text = open(0).read()
head, tail = text.split('\n\n')
mapping = {}
for line in tail.splitlines():
    aa, bb, cc = re.findall(r'[\dA-Z]{3}', line)
    mapping[aa] = [bb, cc]

pos = 'AAA'
steps = itertools.cycle(map('LR'.index, head))
for ans1 in itertools.count(1):
    pos = mapping[pos][next(steps)]
    if pos == 'ZZZ':
        break
print(ans1)

state = [p for p in mapping if p.endswith('A')]
seen = collections.defaultdict(collections.Counter)
steps = itertools.cycle(enumerate(map('LR'.index, head)))
for _ in range(100_000):
    i, step = next(steps)
    state = [mapping[pos][step] for pos in state]
    for j, pos in enumerate(state):
        seen[j][i, pos] += 1
ns = [sum(v > 1 for v in c.values()) for c in seen.values()]
print(math.lcm(*ns))
