import sys
from itertools import combinations


text = sys.stdin.read()
ns = [int(n) for n in text.splitlines()]
for i, n in enumerate(ns):
    if i >= 25 and n not in {a + b for a, b in combinations(ns[:i][-25:], 2)}:
        ans1 = n
print(ans1)


i, j, s = 0, 0, ns[0]
while s != ans1:
    if s < ans1:
        j += 1
        s += ns[j]
    elif s > ans1:
        s -= ns[i]
        i += 1
ans2 = min(ns[i:j]) + max(ns[i:j])
print(ans2)
