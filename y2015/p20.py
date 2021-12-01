from collections import defaultdict
from itertools import count


def divisors(N):
    ds = {1, N}
    for n in range(2, int(N**0.5) + 1):
        if N % n == 0:
            ds.update({n, N // n})
    return ds


lim = int(text)
ans1, ans2 = None, None
n = 830_000
while ans1 is None or ans2 is None:
    ds = divisors(n)
    if ans1 is None and sum(ds) > lim // 10:
        ans1 = n
    if ans2 is None and sum(d for d in ds if n // d <= 50) > lim // 11:
        ans2 = n
    n += 1
