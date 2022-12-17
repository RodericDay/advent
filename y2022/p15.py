import functools
import itertools
import collections


text = open(0).read()
ns = [int(n) for n in ''.join(n if n.isdigit() else ' ' for n in text).split()]
circles = {(x, y, abs(x - a) + abs(y - b)) for x, y , a, b in zip(*[iter(ns)] * 4)}


y_lim = 2_000_000
seen = set()
for x, y, r in circles:
    dy = abs(y_lim - y)
    dx = r - dy
    seen |= set(range(x - dx, x + dx))
print(len(seen))


criss = []
cross = []
for x, y, r in circles:
    p = complex(x, y)
    for i in range(4):
        line = (p + r * 1j ** i), (1j ** (i + 1) + 1j ** (i + 2) ), r + 1
        if i % 2:
            criss.append(line)
        else:
            cross.append(line)


def intersection(l1, l2):
    (p1, d1, r1), (p2, d2, r2) = l1, l2
    for x in range(r1 + 1):
        #  (p1 + d1 * x) = (p2 + d2 * ?)
        if (p1 + d1 * x) - p2 == d2:
            if ((p1 + d1 * x - p2) / d2).real <= r2:
                yield p1 + d1 * x


counter = collections.Counter()
for l1, l2 in itertools.product(criss, cross):
    for p in intersection(l1, l2):
        counter[p] += 1
print(max(counter, key=counter.get))
