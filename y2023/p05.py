import itertools
import pathlib
import re


text = open(0).read()
[seed], *groups = [[[int(n) for n in ln.split()] for ln in group.split(':')[1].strip().splitlines()] for group in text.split('\n\n')]


def forward(n):
    for group in groups:
        n = next((n + (b - a) for b, a, c in group if a <= n < a + c), n)
    return n


ans1 = min([forward(n) for n in seed])
print(ans1)

ns = []
for group in reversed(groups):
    ns += [n for b, a, c in group for n in [b, b + c - 1]]
    ns = [next((n - (b - a) for b, a, c in group if b <= n < b + c), n) for n in ns]
ans2 = min(forward(n) for n in ns if any(a <= n < a + b for a, b in zip(seed[::2], seed[1::2])))
print(ans2)


# old method, slow
def backward(n):
    for group in groups:
        n = next((n - (b - a) for b, a, c in group if b <= n < b + c), n)
    return n

pairs = [(a, a + b) for a, b in zip(seed[::2], seed[1::2])]
next(n for n in itertools.count(ans2) if any(a <= backward(n) < a + b for a, b in pairs))
