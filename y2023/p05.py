import itertools
import pathlib
import re


def forward(n, groups):
    for group in groups:
        for b, a, c in group:
            if a <= n < a + c:
                n = n + (b - a)
                break
    return n


def backward(n, groups):
    for group in reversed(groups):
        for b, a, c in group:
            if b <= n < b + c:
                n = n - (b - a)
                break
    return n


text = open(0).read()
to_matrix = lambda string: [[int(n) for n in ln.split()] for ln in string.splitlines()]
[seed], *groups = [to_matrix(string.split(':')[1].strip()) for string in text.split('\n\n')]

ans1 = min([forward(n, groups) for n in seed])
print(ans1)

ns = []
pairs = [(a, a + b) for a, b in zip(seed[::2], seed[1::2])]
for group in reversed(groups):
    ns += [n for b, a, c in group for n in [b, b + c - 1]]
    ns = [backward(n, [group]) for n in ns]
ans2 = min(forward(n, groups) for n in ns if any(a <= n < b for a, b in pairs))
print(ans2)
