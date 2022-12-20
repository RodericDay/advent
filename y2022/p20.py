from collections import deque


def run(src, cycles=1, factor=1):
    els = deque([(i, int(n) * factor) for i, n in enumerate(src)])
    zero, = [el for el in els if el[1] == 0]
    order = list(els)
    for _ in range(cycles):
        for el in order:
            idx = els.index(el)
            els.rotate(-idx)
            els.popleft()
            els.rotate(-el[1])
            els.appendleft(el)
    idx = els.index(zero)
    els.rotate(-idx)
    return sum(els[n % len(els)][1] for n in [1000, 2000, 3000])


els = open(0).read().splitlines()
print(run(els))
print(run(els, cycles=10, factor=811589153))
