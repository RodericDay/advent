from collections import Counter
from itertools import cycle
from math import copysign


sign = lambda n: int(copysign(1, n))
points = {'flat': Counter(), 'diag': Counter()}
for line in text.splitlines():
    x1, y1, x2, y2 = [int(n) for n in re.findall(r'\d+', line)]
    xs = [*range(x1, x2, sign(x2 - x1)), x2]
    ys = [*range(y1, y2, sign(y2 - y1)), y2]
    if len(xs) == 1:
        points['flat'].update(zip(cycle(xs), ys))
    elif len(ys) == 1:
        points['flat'].update(zip(xs, cycle(ys)))
    else:
        points['diag'].update(zip(xs, ys))
ans1 = sum(v > 1 for v in (points['flat']).values())
ans2 = sum(v > 1 for v in (points['flat'] + points['diag']).values())
