import sys

from intcode import compute


WALL, MOVE, GOAL = range(3)
N, S, W, E = range(1, 5)
ORIENTATIONS = {-1j: N, 1j: S, -1: W, 1: E}

commands = []
command_iter = iter(commands)
text = sys.stdin.read()
bot = compute(text, command_iter)

# hug the wall until we get back home
pos, ori, grid = 0, -1j, {}
while 0 not in grid:
    commands += [ORIENTATIONS[ori]]
    result = next(bot)
    if result == WALL:
        grid[pos + ori] = 1
        ori *= -1j
    else:
        if result == GOAL:
            target = pos
        grid[pos + ori] = 0
        pos += ori
        ori *= 1j

# determine viable spaces
valid = {p for p, v in grid.items() if v == 0}

# from start to end
hops = 0
seen = set()
edge = {0}
while target not in seen:
    hops += 1
    seen |= edge
    edge = {p + d for p in edge for d in ORIENTATIONS} & valid - seen
print(hops)

# from end to all
hops = 0
seen = set()
edge = {target}
while seen != valid:
    hops += 1
    seen |= edge
    edge = {p + d for p in edge for d in ORIENTATIONS} & valid - seen
print(hops)
