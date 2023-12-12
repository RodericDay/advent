def parse(string):
    return {
        complex(x, y): val
        for y, row in enumerate(string.splitlines())
        for x, val in enumerate(row)
    }


def render(grid):
    xmin, *_, xmax = sorted({int(p.real) for p in grid})
    ymin, *_, ymax = sorted({int(p.imag) for p in grid})
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            print(grid[complex(x, y)], end='')
        print()


def rotate(grid, angle):
    swaps_ongoing = 1
    while swaps_ongoing:
        swaps_ongoing = 0
        for pos, val in grid.items():
            if val == 'O':
                while grid.get(pos + angle) == '.':
                    pos, old = pos + angle, pos
                    grid[pos], grid[old] = val, '.'
                    swaps_ongoing += 1
    return grid


def calc_load(state):
    return int(sum(height - p.imag + 1 for p, val in state.items() if val == 'O'))


text = open(0).read()
grid = parse(text)
height = max(p.imag for p in grid)
print(calc_load(rotate(grid, -1j)))

seq = []
while True:
    signature = frozenset(grid.items())
    if signature in seq:
        break
    seq.append(signature)
    for angle in [-1j, -1, 1j, 1]:
        grid = rotate(grid, angle)
prelude = seq.index(signature)
cycle_length = len(seq) - prelude
print(calc_load(dict(seq[prelude + (1_000_000_000 - prelude) % cycle_length])))
