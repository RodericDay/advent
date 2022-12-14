def build_grid(text):
    grid = {}
    for ln in text.splitlines():
        ns = map(int, ''.join(n if n.isdigit() else ' ' for n in ln).split())
        nodes = [complex(x, y) for x, y in zip(*[ns] * 2)]
        for aa, bb in zip(nodes, nodes[1:]):
            step = (bb - aa) / abs(bb - aa)
            while aa != bb:
                grid[aa] = '#'
                aa += step
            grid[aa] = '#'
    return grid


def drip(grid, start, floor, p1=False, dof=[1j, 1j - 1, 1j + 1]):
    pos = start
    while True:
        for new in (pos + step for step in dof):
            if new not in grid and new.imag != floor:
                pos = new
                break
        else:
            grid[pos] = 'o'
            yield True
            pos = start

        if p1:
            if pos.imag == floor - 1:
                break
        else:
            if grid.get(start) == 'o':
                break


def main():
    text = open(0).read()
    grid = build_grid(text)
    start = complex(500, 0)
    floor = max(p.imag for p in grid) + 2

    ans1 = sum(drip(grid.copy(), start, floor, True))
    print(ans1)

    ans2 = sum(drip(grid.copy(), start, floor))
    print(ans2)


main()
