from itertools import combinations, product


def manhattan(p1, p2):
    return tuple(abs(a - b) for a, b in zip(p1, p2))


def find_shared_transpose(pts):
    new = {manhattan(a, b): a for a, b in combinations(pts, 2)}
    deltas = [
        [(a - b) for a, b in zip(constellations[k], new[k])]
        for k in set(constellations) & set(new)
    ]
    if deltas:
        return [max(t, key=t.count) for t in zip(*deltas)]


def overlap(pts):
    for fx, fy, fz in product([1, -1], [1, -1], [1, -1]):
        flipped = {(x * fx, y * fy, z * fz) for x, y, z in pts}
        if deltas := find_shared_transpose(flipped):
            dx, dy, dz = deltas
            transposed = {(x + dx, y + dy, z + dz) for x, y, z in flipped}
            if len(all_beacons & transposed) >= 12:
                update_state((-dx, -dy, -dz), transposed)
                return True


def update_state(scanner, beacons):
    all_scanners.add(scanner)
    all_beacons.update(beacons)
    new = {manhattan(a, b): a for a, b in combinations(all_beacons, 2)}
    constellations.update(new)


def transform(step, pts):
    if step % 3 == 0:
        pts = [pt[::-1] for pt in pts]
    return [pt[1:] + pt[:1] for pt in pts]


text = open(0).read()
reference, *readings = [
    [tuple(int(n) for n in ln.split(',')) for ln in scnr.splitlines()[1:]]
    for scnr in text.split('\n\n')
]
all_scanners = set()
all_beacons = set()
constellations = {}
update_state((0, 0, 0), reference)
for step in range(30):
    readings = [transform(step, pts) for pts in readings if not overlap(pts)]
print(len(all_beacons))
print(max(sum(manhattan(a, b)) for a, b in combinations(all_scanners, 2)))
