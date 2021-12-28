ns = [int(n) for n in open(0).read().split(',')]
lo, *_, hi = sorted(ns)

def mono_min(g):
    y = next(g)
    for x in g:
        if x > y: return y
        y = x

print(mono_min(sum(abs(n - m) for m in ns) for n in range(lo, hi)))
range_sum = lambda n: int(n * (n + 1) / 2)
print(mono_min(sum(range_sum(abs(n - m)) for m in ns) for n in range(lo, hi)))
