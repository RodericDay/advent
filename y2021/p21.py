from functools import lru_cache
from itertools import product, cycle, count


@lru_cache(maxsize=None)
def play(p1, p2, s1=0, s2=0):
    if s2 >= 21: return 0, 1
    w1, w2 = 0, 0
    for die in d3:
        pN = (p1 + die) % 10 or 10
        n2, n1 = play(p2, pN, s2, s1 + pN)
        w1, w2 = (w1 + n1), (w2 + n2)
    return w1, w2


text = open(0).read()
d3 = [sum(rolls) for rolls in product(range(1, 4), repeat=3)]
p1, p2 = [int(ln[-1]) for ln in text.splitlines()]

state = {0: (0, p1), 1: (0, p2)}
d100 = cycle(range(1,101))
for i in count():
    score, pos = state[i % 2]
    pos = (pos + next(d100) + next(d100) + next(d100)) % 10 or 10
    state[i % 2] = (score + pos, pos)
    if score + pos >= 1000:
        break
print((i + 1) * 3 * min(state.values())[0])

print(max(play(p1, p2)))
