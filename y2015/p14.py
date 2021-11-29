import collections
import itertools


reindeers = [
    itertools.accumulate(itertools.cycle([speed] * act + [0] * rest))
    for line in df.read_text().splitlines()
    for speed, act, rest in [map(int, re.findall(r'\d+', line))]
]


traveled = [[next(rr) for _ in range(2503)] for rr in reindeers]
transpose = list(zip(*traveled))
ans1 = max(transpose[-1])
points = [[d == max(dsts) for d in dsts] for dsts in transpose]
ans2 = max(sum(pts) for pts in zip(*points))
