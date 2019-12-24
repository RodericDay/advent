import itertools
import sys

from toolkit import read_image, shortest_path


def move(pos):
    for adj in (pos + ori for ori in [1, -1, 1j, -1j]):
        if adj in grid:
            yield adj
        if adj in duals:
            yield from move(duals[adj])


def move_with_depth(state):
    pos, level = state
    for adj in (pos + ori for ori in [1, -1, 1j, -1j]):
        if adj in inner:
            yield from move_with_depth((duals[adj], level + 1))
        elif adj in outer and (level > 0) and (grid[adj] not in {'AA', 'ZZ'}):
            yield from move_with_depth((duals[adj], level - 1))
        elif adj in grid:
            yield adj, level


# base
text = sys.stdin.read()
grid = {pos: val for pos, val in read_image(text).items() if val not in ' #'}
for pos, val in grid.copy().items():
    if val.isupper():
        for im in [1, 1j]:
            A, B, C = [pos - im, pos, pos + im]
            if grid.get(C) == '.':
                grid[B] = grid.pop(A) + grid.pop(B)
            if grid.get(A) == '.':
                grid[B] = grid.pop(B) + grid.pop(C)
elements = {v: k for k, v in grid.items()}

# matrix
duals = {}
portals = {pos for pos, cell in grid.items() if cell.isupper()}
for pA, pB in itertools.combinations(portals, 2):
    if grid[pA] == grid[pB]:
        duals[pA] = pB
        duals[pB] = pA

# part1
start, end = elements['AA'], elements['ZZ']
path = shortest_path(start, end, move)
print(len(path) - 3)

# categorize portals
_, *xmid, _ = sorted({p.real for p in portals})
_, *ymid, _ = sorted({p.imag for p in portals})
inner = {pos for pos in portals if pos.real in xmid and pos.imag in ymid}
outer = set(portals) - inner

# part2
start, end = (elements['AA'], 0), (elements['ZZ'], 0)
path = shortest_path(start, end, move_with_depth)
print(len(path) - 3)
