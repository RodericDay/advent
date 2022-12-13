def parse_grid(text):
    grid = {}
    for y, row in enumerate(text):
        for x, v in enumerate(row):
            grid[complex(x, y)] = v if v in 'SE' else ord(v)
    return grid


def print_grid(mapping):
    xmin, *_, xmax = {int(p.real) for p in mapping}
    ymin, *_, ymax = {int(p.imag) for p in mapping}
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            print(mapping.get(complex(x, y), ' '), end=' ')
        print()


def shortest_path(starts, ends, evolve):
    starts = {k: [k] for k in starts}
    known = starts.copy()
    while starts:
        old = list(starts)[0]
        path = starts.pop(old)
        starts |= {new: path + [new] for new in evolve(old) if new not in known}
        known |= starts
        for final in set(starts) & set(ends):
            # print_grid({k: '.' for k in known[final]})
            return known[final]


def main():
    text = open(0).read().splitlines()
    grid = parse_grid(text)

    rev = {v: k for k, v in grid.items()}
    start, end = rev['S'], rev['E']
    grid[start], grid[end] = ord('a'), ord('z')

    dof = [1, -1, 1j, -1j]
    evolve = lambda old: {old + step for step in dof if is_valid(old, step)}
    is_valid = lambda old, step: old + step in grid and grid[old + step] - grid[old] <= 1

    print(len(shortest_path({start}, {end}, evolve)) - 1)
    starts = {k for k, v in grid.items() if v == ord('a')}
    print(len(shortest_path(starts, {end}, evolve)) - 1)


main()
