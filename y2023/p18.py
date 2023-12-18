def render(graph):
    xmin, *_, xmax = sorted(int(p.real) for p in walls)
    ymin, *_, ymax = sorted(int(p.imag) for p in walls)
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            print('#' if complex(x, y) in graph else '.', end='')
        print()


text = open(0).read()

walls = {0}
pos = 0
for line in text.splitlines():
    d, n, rest = line.split()
    n, d = int(rest[1:-1][1:][:5], 16), 'RDLU'[int(rest[-2])]
    pos += {'R': 1, 'D': 1j, 'L': -1, 'U': -1j}[d] * int(n)
    walls.add(pos)

smallx = {v: i * 2 for i, v in enumerate(sorted({p.real for p in walls}))}
smally = {v: i * 2 for i, v in enumerate(sorted({p.imag for p in walls}))}
walls = {complex(smallx[p.real], smally[p.imag]) for p in walls}


walls = {0}
pos = 0
smallpos = 0
for line in text.splitlines():
    d, n, rest = line.split()
    n, d = int(rest[1:-1][1:][:5], 16), 'RDLU'[int(rest[-2])]
    pos += {'R': 1, 'D': 1j, 'L': -1, 'U': -1j}[d] * int(n)
    goal = complex(smallx[pos.real], smally[pos.imag])
    dirx = (goal - smallpos).real or (goal - smallpos).imag
    while smallpos != goal:
        smallpos += dirx
        walls.add(smallpos)


render(walls)
exit()


xmin, *_, xmax = sorted(int(p.real) for p in walls)
ymin, *_, ymax = sorted(int(p.imag) for p in walls)
void = {complex(x, y) for x in range(xmin, xmax + 1) for y in range(ymin, ymax + 1)} - walls

groups = []
while void:
    seen = set()
    edge = {void.pop()}
    while edge:
        seen |= edge
        edge = {pp + ss for pp in edge for ss in [1, -1, 1j, -1j]} & void - seen
    groups.append(seen)
    void -= seen

inside = {p for g in groups if not any(p.real in {xmin, xmax} or p.imag in {ymin, ymax} for p in g) for p in g}
print(len(inside | walls))
