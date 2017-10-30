    import re
    import itertools
    import functools
    import collections
    import operator

    text = open('challenge_15.txt').read().strip().split('\n')

    total = 100
    things = {}
    for line in text:
        ing, stuff = line.split(':')
        things[ing] = {k:int(v) for prop in stuff.split(',') for k, v in [prop.strip().split(' ')]}

    def tally(combo):
        total = collections.Counter()
        for ing, n in combo.items():
            for k, v in things[ing].items():
                total[k] += n*v
        for k, v in total.items():
            if v < 0:
                total[k] = 0
        calories = total['calories']
        total['calories'] = 1
        # part 2
        if calories != 500: total['calories'] = 0
        return functools.reduce(operator.mul, total.values())

    def partition(N, d):
        if d==1: yield [N]
        else: yield from ( [H]+T for H in range(N+1) for T in partition(N-H, d-1) )

    best = 0
    for combo in (dict(zip(things, combo)) for combo in partition(100, 4)):
        total = tally(combo)
        if total > best:
            best = total
    print(best)
