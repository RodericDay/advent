import sys


text = sys.stdin.read()
pairs = [tuple(map(int, line.split('-'))) for line in text.splitlines()]
valid, lo, hi = [], 0, 0
for a, b in sorted(pairs):
    if a > hi:
        valid.extend(range(hi + 1, a))
        lo, hi = a, b
    lo, hi = min(lo, a), max(hi, b)
print(valid[0])
print(len(valid))
