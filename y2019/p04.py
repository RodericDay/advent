import sys
import itertools

strings = [str(n) for n in range(347312, 805915 + 1)]
print(sum(list(s) == sorted(s) and any(len(list(vs)) >= 2 for k, vs in itertools.groupby(s)) for s in strings))
print(sum(list(s) == sorted(s) and any(len(list(vs)) == 2 for k, vs in itertools.groupby(s)) for s in strings))
