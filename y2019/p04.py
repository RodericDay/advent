import sys
from itertools import groupby


A, B = [int(n) for n in sys.stdin.read().split('-')]
strings = [str(n) for n in range(A, B + 1)]
print(sum(list(s) == sorted(s) and any(len(list(vs)) >= 2 for k, vs in groupby(s)) for s in strings))  # noqa
print(sum(list(s) == sorted(s) and any(len(list(vs)) == 2 for k, vs in groupby(s)) for s in strings))  # noqa
