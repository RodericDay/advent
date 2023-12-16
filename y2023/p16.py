def reflect(pos, dirx):
    match '-' if dirx.real else '|', graph.get(pos, ' '):
        case [_, ' ']: return []
        case [_, '.']: return [0]
        case ['-', '-']: return [0]
        case ['-', 'L']: return [1]
        case ['-', '/']: return [-1]
        case ['-', '|']: return [1, -1]
        case ['|', '|']: return [0]
        case ['|', '/']: return [1]
        case ['|', 'L']: return [-1]
        case ['|', '-']: return [1, -1]
        case other: raise RuntimeError(other)


def solve(start):
    seen = set()
    state = {start}
    while state:
        seen |= state
        state = {(pp + dd * 1j ** rr, dd * 1j ** rr) for pp, dd in state for rr in reflect(pp, dd)} - seen
    return len({x for x, y in seen} & set(graph))


text = open(0).read().replace('\\', 'L')
graph = {
    complex(x, y): val
    for y, row in enumerate(text.splitlines())
    for x, val in enumerate(row)
}
print(solve((0, 1)))

xmin, *_, xmax = sorted(int(p.real) for p in graph)
ymin, *_, ymax = sorted(int(p.imag) for p in graph)
starts = []
starts += [(complex(x, ymin), 1j) for x in range(xmin, xmax + 1)]
starts += [(complex(x, ymax),-1j) for x in range(xmin, xmax + 1)]
starts += [(complex(xmin, y), 1 ) for y in range(ymin, ymax + 1)]
starts += [(complex(xmax, y),-1 ) for y in range(ymin, ymax + 1)]
print(max(solve(start) for start in starts))
