import itertools


# transform text into two helpful data structures
valid = set()
special_locations = {}
for y, line in enumerate(data_file.read_text().splitlines()):
    for x, char in enumerate(line):
        if char != '#':
            valid.add((x, y))
            if char != '.':
                special_locations[(x, y)] = char


# generate travel graph from every starting point to every other point via BFS
graph = {}
steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for A in special_locations:
    seen = {A}
    boundary = {A}
    locations_pending = set(special_locations) - seen
    for n_steps_taken in itertools.count(1):
        boundary = {(x + dx, y + dy) for x, y in boundary for dx, dy in steps}
        boundary &= valid - seen
        seen.update(boundary)
        for B in boundary & locations_pending:
            locations_pending -= {B}
            graph[special_locations[A], special_locations[B]] = n_steps_taken
        if not locations_pending:
            break


# use map to determine routes
z = '0'
not_z = set(special_locations.values()) - {z}
calc = lambda combo: sum(graph[a, b] for a, b in zip(combo, combo[1:]))
ans1 = min(calc((z, *combo)) for combo in itertools.permutations(not_z))
ans2 = min(calc((z, *combo, z)) for combo in itertools.permutations(not_z))
