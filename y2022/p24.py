def loop(p, drx):
    p += drx
    if p not in grid:
        p -= drx * (H if drx.imag else W)
    return p


def blizzards(n, cache={}, valid={'>': 1, '<': -1, '^': -1j, 'v': 1j}):
    if n not in cache:
        if n == 0:
            cache[n] = [(p, valid[c]) for p, c in grid.items() if c != '.']
        else:
            cache[n] = [(loop(p, drx), drx) for p, drx in blizzards(n - 1)]
    return cache[n]


def bfs(starts, ends, tt=0, dir5=[0, 1, -1j, -1, 1j]):
    edge = starts
    while not ends & edge:
        tt += 1
        blizz = {p for p, _ in blizzards(tt)}
        edge = {p + dp for p in edge for dp in dir5} & set(grid) - blizz
    return tt


def main():
    global grid, W, H

    rows = open(0).read().splitlines()
    grid = {complex(x, y): c for y, r in enumerate(rows)
                             for x, c in enumerate(r) if c != '#'}

    H, W = len(rows) - 2, len(rows[1]) - 2
    start, *_, end = sorted(grid, key=lambda p: (p.imag, p.real))

    t1 = bfs({start}, {end})
    print(t1)

    t2 = bfs({end}, {start}, t1)
    t3 = bfs({start}, {end}, t2)
    print(t3)


main()
