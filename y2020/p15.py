import collections
import itertools
import sys


text = sys.stdin.read()
inp = [int(n) for n in text.split(',')][::-1]
seen = collections.defaultdict(lambda: collections.deque(maxlen=2))
spoken = None
for turn in itertools.count(1):
    if inp:
        spoken = inp.pop()
    elif len(seen[spoken]) < 2:
        spoken = 0
    else:
        spoken = seen[spoken][-1] - seen[spoken][-2]

    if turn == 2020:
        print(spoken)
    elif turn == 30_000_000:
        print(spoken)
        break

    seen[spoken].append(turn)
