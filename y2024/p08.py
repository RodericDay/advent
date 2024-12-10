import collections
import itertools


inp = open(0).read()

grid = {complex(x, y): cell for y, row in enumerate(inp.splitlines()) for x, cell in enumerate(row)}

coll = collections.defaultdict(set)
for k, v in grid.items():
    if v != '.':
        coll[v].add(k)

map1 = set()
map2 = set()
for _, vs in coll.items():
    for p1, p2 in itertools.combinations(vs, 2):
        dp = p1 - p2
        map1 |= {p1 + dp, p2 - dp}.intersection(grid)
        map2 |= {p1 + i * dp for i in range(-50, 50)}.intersection(grid)

print(len(map1))
print(len(map2))
