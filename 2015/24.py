import itertools, operator, functools

with open('24.txt') as fp:
    ns = [int(n) for n in fp.read().splitlines()]

def knapsack(ns, goal=sum(ns)//3, good=[]):
    if goal == 0:
        yield good
    if goal > 0 and len(good) < 6:
        for i, n in enumerate(ns):
            yield from knapsack(ns[i+1:], goal-n, good+[n])

def QE(combo):
    return functools.reduce(operator.mul, combo)

ans = min((len(combo), QE(combo), combo) for combo in knapsack(ns))
print(ans)
