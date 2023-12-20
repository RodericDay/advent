def perimeter(pts):
    n = 0
    for i in range(len(pts)):
        dist = pts[i - 1] - pts[i]
        n += abs(dist.real) + abs(dist.imag)
    return int(n / 2) + 1


def area(pts):
    # shoelace method
    a = 0
    for i in range(len(pts)):
        p1, p2 = pts[i - 1], pts[i]
        a += p1.real * p2.imag - p2.real * p1.imag
    return int(a / 2)


text = open(0).read()

pts = [0]
for line in text.splitlines():
    d, n, _ = line.split()
    n = int(n)
    d = 1j ** 'RDLU'.index(d)
    pts.append(pts[-1] + d * n)
print(area(pts) + perimeter(pts))

pts = [0]
for line in text.splitlines():
    _, _, s = line.split()
    n = int(s[2:7], 16)
    d = 1j ** int(s[7])
    pts.append(pts[-1] + d * n)
print(area(pts) + perimeter(pts))


# def render(graph, default='.'):
#     xmin, *_, xmax = sorted(int(p.real) for p in graph)
#     ymin, *_, ymax = sorted(int(p.imag) for p in graph)
#     out = ''
#     for y in range(ymin, ymax + 1):
#         for x in range(xmin, xmax + 1):
#             out += graph.get(complex(x, y), default)
#         out += '\n'
#     return out


# def connected_components(graph):
#     groups = []
#     while graph:
#         seen = set()
#         edge = {graph.pop()}
#         while edge:
#             seen |= edge
#             edge = {pp + ss for pp in edge for ss in [1, -1, 1j, -1j] if pp + ss in graph if pp + ss not in seen}
#         groups.append(seen)
#         graph -= seen
#     return groups


# def get_solid(walls):
#     xmin, *_, xmax = sorted(int(p.real) for p in walls)
#     ymin, *_, ymax = sorted(int(p.imag) for p in walls)

#     mesh = {complex(x, y) for x in range(xmin, xmax + 1) for y in range(ymin, ymax + 1)}
#     void = mesh - walls
#     groups = connected_components(void)
#     border = lambda p: p.real in {xmin, xmax} or p.imag in {ymin, ymax}
#     inside = {p for g in groups if not any(border(p) for p in g) for p in g}
#     solid = inside | walls
#     return solid


# def solve1():
#     pos = 0
#     walls = {pos}
#     for line in text.splitlines():
#         d, n, _ = line.split()
#         dirx = 1j ** 'RDLU'.index(d)
#         goal = pos + dirx * int(n)
#         while pos != goal:
#             pos += dirx
#             walls.add(pos)
#     solid = get_solid(walls)
#     print(len(solid))


# def solve2():
#     points = {0}
#     pos = 0
#     for line in text.splitlines():
#         _, _, rest = line.split()
#         n, d = int(rest[1:-1][1:][:5], 16), 'RDLU'[int(rest[-2])]
#         dirx = 1j ** 'RDLU'.index(d)
#         pos += dirx * int(n)
#         points.add(pos)

#     b2s = {
#         complex(bx, by) + dx + dy: 3 * complex(sx, sy) + dx + dy
#         for sx, bx in enumerate(sorted({p.real for p in points}))
#         for sy, by in enumerate(sorted({p.imag for p in points}))
#         for dx in [-1, 0, 1] for dy in [-1j, 0, 1j]
#     }
#     s2b = {v: k for k, v in b2s.items()}

#     pos, smallpos = 0, b2s[0]
#     walls = {smallpos}
#     for line in text.splitlines():
#         d, n, rest = line.split()
#         n, d = int(rest[1:-1][1:][:5], 16), 'RDLU'[int(rest[-2])]
#         dirx = 1j ** 'RDLU'.index(d)
#         pos += dirx * int(n)
#         goal = b2s[pos]
#         while smallpos != goal:
#             smallpos += dirx
#             walls.add(smallpos)

#     solid = get_solid(walls)

#     out = 0
#     for smallpos in solid:
#         c1, c2 = s2b[smallpos], s2b[smallpos + 1 + 1j]
#         w, h = (c2 - c1).real, (c2 - c1).imag
#         out += int(w * h)
#     print(out)


# text = open(0).read()
# solve1()
# solve2()
