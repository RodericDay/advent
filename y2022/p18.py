def move(pt):
    x, y, z = pt
    for dx in [1, 0, -1]:
        for dy in [1, 0, -1]:
            for dz in [1, 0, -1]:
                if abs(dx) + abs(dy) + abs(dz) == 1:
                    yield x + dx, y + dy, z + dz


def is_outside(pt, outside=set(), inside=set(), max_bubble_size=2000):
    edge = {pt}
    seen = set()
    while True:
        edge = {adj_pt for pt in edge for adj_pt in move(pt)} - seen - cubes
        seen |= edge
        if seen & outside or len(seen) > max_bubble_size:
            outside |= seen
            return True
        if seen & inside or not edge:
            inside |= seen
            return False


def solve(is_outside=lambda *args: True):
    surface = 0
    for pt in cubes:
        for adj_pt in move(pt):
            if adj_pt not in cubes and is_outside(adj_pt):
                surface += 1
    return surface


text = open(0).read()
cubes = {tuple(map(int, ln.split(','))) for ln in text.splitlines()}
print(solve())
print(solve(is_outside))
