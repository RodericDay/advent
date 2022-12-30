import re
import itertools


text = open(0).read()
graph = {}
vals = {}
for ln in text.splitlines():
    pos, val, *adjs = re.findall(r'[A-Z]{2}|\d+', ln)
    if int(val):
        vals[pos] = int(val)
    graph[pos] = {k: 1 for k in adjs}
old = {k: v.copy() for k, v in graph.items()}


for k in graph:
    graph[k][k] = 0
    edge = {k}
    seen = set()
    for step in range(1, 1000):
        edge = {n for k in edge for n in old[k]} - seen
        seen |= edge
        for n in edge:
            graph[k].setdefault(n, step)


def tic(pending, start, left):
    out = []
    for end in pending:
        rem = max(0, left - graph[start][end] - 1)
        out.append([vals[end] * rem, end, rem])
    return sorted(out, reverse=True)


def solve1(pending, total, pos, t_left):
    if not pending:
        yield total
    else:
        if ans1 > total + sum(vals[p] for p in pending) * t_left:
            return
        for contrib, pos, t_left in tic(pending, pos, t_left):
            yield from solve1(pending - {pos}, total + contrib, pos, t_left)


ans1 = 0
for ans in solve1(set(vals), 0, 'AA', 30):
    if ans > ans1:
        ans1 = ans
print(ans1)


def solve2(pending, total, pos_1, t_left_1, pos_2, t_left_2):
    if not pending:
        yield total
    else:
        if ans2 > total + sum(vals[p] for p in pending) * max(t_left_1, t_left_2):
            return
        if t_left_1 >= t_left_2:
            # move 1
            for contrib, pos, t_left in tic(pending, pos_1, t_left_1):
                yield from solve2(pending - {pos}, total + contrib, pos, t_left, pos_2, t_left_2)
        else:
            # move 2
            for contrib, pos, t_left in tic(pending, pos_2, t_left_2):
                yield from solve2(pending - {pos}, total + contrib, pos_1, t_left_1, pos, t_left)


ans2 = 0
for ans in solve2(set(vals), 0, 'AA', 26, 'AA', 26):
    if ans > ans2:
        ans2 = ans
print(ans2)
