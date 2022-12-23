rows = open(0).read().splitlines()
grid = {complex(x, y) for y, l in enumerate(rows)
                      for x, c in enumerate(l) if c in '#'}
dir8 = {dx + dy for dx in [-1, 0, 1]
                for dy in [-1j, 0, 1j] if not dx + dy == 0}
dir3 = [(k, {k, k + k * 1j, k - k * 1j}) for k in [-1j, 1j, -1, 1]]


def render(grid):
    xmin, *_, xmax = sorted(int(p.real) for p in grid)
    ymin, *_, ymax = sorted(int(p.imag) for p in grid)
    sab = ''
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            sab += grid.get(complex(x, y), ' ')
        sab += '\n'
    return sab


def look(p):
    for k, ds in dir3:
        if not {p + d for d in ds} & grid:
            return p + k


for i in range(1, 100000):

    moves = {}
    for p in grid:
        if not any(p + dp in grid for dp in dir8):
            continue
        moves.setdefault(look(p), []).append(p)
    dir3 = dir3[1:] + dir3[:1]

    if not moves:
        print(i)
        break

    for k, vs in moves.items():
        if k is not None:
            if len(vs) == 1:
                grid = grid - set(vs) | {k}

    if i == 10:
        print(render({k: '#' for k in grid}).count(' '))
