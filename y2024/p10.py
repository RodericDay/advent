import collections

inp = open(0).read()

grid = {complex(x, y): int(cell) for y, row in enumerate(inp.splitlines()) for x, cell in enumerate(row) if cell.isdigit()}

def trail1(start):
    edge = {start}
    seen = set()
    while edge:
        edge = {p + dp for p in edge for dp in [1, -1, 1j, -1j] if p + dp in grid and grid[p + dp] - grid[p] == 1} - seen
        seen |= edge
    return sum(grid[k] == 9 for k in seen)

def backtrack(k, parents):
    if not parents[k]:
        yield 1
    else:
        for k in parents[k]:
            yield from backtrack(k, parents)

def trail2(start):
    edge = {start}
    parents = collections.defaultdict(set)
    seen = set()
    while edge:
        for p in edge:
            for dp in [1, -1, 1j, -1j]:
                if (p + dp in grid) and (grid[p + dp] - grid[p] == 1):
                    parents[p + dp].add(p)
        edge = set(parents) - seen
        seen |= edge
    return sum(sum(backtrack(k, parents)) for k in seen if grid[k] == 9)

print(sum(trail1(k) for k, v in grid.items() if v == 0))
print(sum(trail2(k) for k, v in grid.items() if v == 0))
