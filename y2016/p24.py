import sys
from itertools import permutations


text = sys.stdin.read()


# transform text into data structures
valid = set()
target = {}
for y, line in enumerate(text.splitlines()):
    for x, char in enumerate(line):
        if char == '#':
            continue
        valid.add(x + 1j * y)
        if char != '.':
            target[x + 1j * y] = char


# generate travel map
graph = {}
for A in target:
    seen = {A}
    boundary = {A}
    pending = set(target) - seen
    N = 0
    while pending:
        N += 1
        boundary = {pos + step for pos in boundary for step in [1, -1, 1j, -1j]}
        boundary &= valid - seen
        seen.update(boundary)

        for B in boundary & pending:
            pending -= {B}
            graph[target[A], target[B]] = N


# use map to determine routes
calc = lambda combo: sum(graph[pair] for pair in zip(combo, combo[1:]))

z = '0'
rest = set(target.values()) - {z}
options = [(z,) + combo for combo in permutations(rest)]
ans = min(options, key=calc)
print(calc(ans))

options = [(z,) + combo + (z,) for combo in permutations(rest)]
ans = min(options, key=calc)
print(calc(ans))
