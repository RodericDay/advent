ns = [int(n) for n in text.split(',')]
lo, *_, hi = sorted(ns)

def mono_min(g):
    y = next(g)
    for x in g:
        if x > y: return y
        y = x

ans1 = mono_min(sum(abs(n - m) for m in ns) for n in range(lo, hi))
range_sum = lambda n: int(n * (n + 1) / 2)
ans2 = mono_min(sum(range_sum(abs(n - m)) for m in ns) for n in range(lo, hi))
