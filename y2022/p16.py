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
