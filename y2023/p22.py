@lambda fn: lambda brick: set(fn(brick))
def dimension(brick):
    (x1, x2), (y1, y2), (z1, z2) = map(sorted, zip(*brick))
    for z in range(z1, z2 + 1):
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                yield x, y, z


def tetris(bricks):
    floor = {(x, y, 0) for x in range(100) for y in range(100)}
    seen = floor
    for brick in map(dimension, bricks):
        while not seen & brick:
            brick = {(x, y, z - 1) for x, y, z in brick}
        resting_place = {(x, y, z + 1) for x, y, z in brick}
        seen |= resting_place
        yield resting_place


def topple(i, depends_on, holds_up):
    gone = set()
    state = {i}
    while state:
        gone |= state
        state = {above
            for below in state
            for above in depends_on.get(below, [])
            if holds_up[above] <= gone
        }
    return gone - {i}


text = open(0).read()
bricks = [[[int(n) for n in sub.split(',')] for sub in line.split('~')] for line in text.splitlines()]
bricks.sort(key=lambda brick: min(z for x, y, z in brick))
bricks = list(tetris(bricks))

known = {i for i, _ in enumerate(bricks)}
holds_up, depends_on = {}, {}
for j, brick in enumerate(bricks):
    j_brick_1_down = {(x, y, z - 1) for x, y, z in brick}
    holds_up[j] = {i for i, i_brick in enumerate(bricks) if i != j and j_brick_1_down & i_brick}
    for i in holds_up[j]:
        depends_on.setdefault(i, set()).add(j)

needed = {v for k, vs in holds_up.items() if len(vs) == 1 for v in vs}
print(len(known - needed))
print(sum(len(topple(i, depends_on, holds_up)) for i in needed))
