grid = {}
for y, line in enumerate(open(0)):
    for x, char in enumerate(line[:-1]):
        grid[complex(x, y)] = char

ans1 = 0
for p, v in grid.items():
    if all(grid[p + s] > v for s in [1, -1, 1j, -1j] if p + s in grid):
        ans1 += int(v) + 1
print(ans1)

valid = {k for k, v in grid.items() if v != '9'}
pending = valid.copy()
basin_sizes = []
while pending:
    edge = {pending.pop()}
    seen = edge.copy()
    while edge:
        edge = {p + s for p in edge for s in [1, -1, 1j, -1j]} & valid - seen
        seen |= edge
    pending -= seen
    basin_sizes.append(len(seen))
*_, x, y, z = sorted(basin_sizes)
print(x * y * z)
