import collections
import itertools
import re
import sys


text = sys.stdin.read()
dqs = []
for line in text.splitlines():
    k, ps, _, i = map(int, re.findall(r'\d+', line))
    dq = collections.deque(range(ps))
    dq.rotate(-i - k + 1)
    dqs.append(dq)

for i in itertools.count():
    for dq in dqs:
        dq.rotate(-1)
    if len({dq[0] for dq in dqs}) == 1:
        break
print(i)
