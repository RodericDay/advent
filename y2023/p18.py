def render(graph, default='.'):
    xmin, *_, xmax = sorted(int(p.real) for p in walls)
    ymin, *_, ymax = sorted(int(p.imag) for p in walls)
    out = ''
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            out += graph.get(complex(x, y), default)
        out += '\n'
    return out


def connected_components(graph):
    groups = []
    while graph:
        seen = set()
        edge = {graph.pop()}
        while edge:
            seen |= edge
            edge = {pp + ss for pp in edge for ss in [1, -1, 1j, -1j]} & graph - seen
        groups.append(seen)
        graph -= seen
    return groups


text = open(0).read()
p2 = True

walls = {0}
pos = 0
for line in text.splitlines():
    d, n, rest = line.split()
    if p2:
        n, d = int(rest[1:-1][1:][:5], 16), 'RDLU'[int(rest[-2])]
    pos += {'R': 1, 'D': 1j, 'L': -1, 'U': -1j}[d] * int(n)
    walls.add(pos)

b2s = {
    complex(bx, by) + dx + dy: 3 * complex(sx, sy) + dx + dy
    for sx, bx in enumerate(sorted({p.real for p in walls}))
    for sy, by in enumerate(sorted({p.imag for p in walls}))
    for dx in [-1, 0, 1] for dy in [-1j, 0, 1j]
}

pos, smallpos = next(iter(b2s.items()))
walls = {smallpos}
for line in text.splitlines():
    d, n, rest = line.split()
    if p2:
        n, d = int(rest[1:-1][1:][:5], 16), 'RDLU'[int(rest[-2])]
    dirx = {'R': 1, 'D': 1j, 'L': -1, 'U': -1j}[d]
    pos += dirx * int(n)
    goal = b2s[pos]
    while smallpos != goal:
        smallpos += dirx
        walls.add(smallpos)

xmin, *_, xmax = sorted(int(p.real) for p in b2s.values())
ymin, *_, ymax = sorted(int(p.imag) for p in b2s.values())
void = {complex(x, y) for x in range(xmin, xmax + 1) for y in range(ymin, ymax + 1)} - walls
groups = connected_components(void)
inside = {p for g in groups if not any(p.real in {xmin, xmax} or p.imag in {ymin, ymax} for p in g) for p in g}
solid = inside | walls

# print(render({k: '#' for k in solid}))

s2b = {v: k for k, v in b2s.items()}
out = 0
for smallpos in solid:
    c1, c2 = s2b[smallpos], s2b[smallpos + 1 + 1j]
    w, h = (c2 - c1).real, (c2 - c1).imag
    out += int(w * h)
print(out)
