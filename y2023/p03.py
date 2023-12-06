import math
import collections
import itertools
import re


text = open(0).read()
grid = collections.defaultdict(str) | {
    (x, y): cell
    for y, line in enumerate(text.splitlines())
    for x, cell in enumerate(line)
}
parts = collections.defaultdict(list)

ans1 = 0
for y, ln in enumerate(text.splitlines()):
    ys = [y - 1, y, y + 1]
    for match in re.finditer(r'\d+', ln):
        N = int(match.group(0))
        xs = list(range(match.start() - 1, match.end() + 1))

        sub = {(x, y): grid[x, y] for x in xs for y in ys}
        if set(sub.values()) - set('0123456789\n.'):
            ans1 += N

        for key, value in sub.items():
            if value == '*':
                parts[key].append(N)
print(ans1)

ans2 = sum(math.prod(values) for values in parts.values() if len(values) == 2)
print(ans2)
