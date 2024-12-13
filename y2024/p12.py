import collections

inp = open(0).read()

grid = {complex(x, y): cell for y, row in enumerate(inp.splitlines()) for x, cell in enumerate(row)}

groups = []
links = collections.defaultdict(set)
while grid:
    pos, cell = grid.popitem()
    edge = {pos}
    seen = edge.copy()
    while edge:
        tmp = set()
        for p in edge:
            for dp in [1, -1, 1j, -1j]:
                if grid.get(p + dp) == cell:
                    tmp.add(p + dp)
                    links[p].add(p + dp)
                    links[p + dp].add(p)
        edge = tmp - seen
        seen |= edge
    grid = {k: v for k, v in grid.items() if k not in seen}
    groups.append((cell, seen))

def perimeter(group):
    return sum(4 - len(links[p]) for p in group)

def perimeter2(group):
    border = set()
    for p in group:
        for dp in [1, -1, 1j, -1j]:
            if p + dp not in group:
                border.add((p, dp))

    cnt = 0
    while border:
        p = border.pop()
        edge = {p}
        seen = edge.copy()
        while edge:
            edge = {(p + step, dp) for (p, dp) in edge for step in [1, -1, 1j, -1j]} & border - seen
            seen |= edge
        border -= seen
        cnt += 1
    return cnt

print(sum(len(group) * perimeter(group) for _, group in groups))
print(sum(len(group) * perimeter2(group) for _, group in groups))
