import sys
from itertools import count

import toolkit


text = sys.stdin.read()


tid, string = text.split()
tid = int(tid)
found = [
    next((tid + i, val) for i in count() if (tid + i) % val == 0)
    for val in [int(v) for v in string.split(',') if v != 'x']
]
a, b = min(found)
print((a - tid) * b)


args = [(i, int(val)) for i, val in enumerate(string.split(',')) if val != 'x']
(last, step), *tail = args
for offset, val in tail:
    last += next(i for i in count(step=step) if (last + i + offset) % val == 0)
    step = toolkit.lcm(step, val)
print(last)
