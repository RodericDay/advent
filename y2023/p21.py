def bfs_twinkle(start, graph, cycles):
    seen = [set()]
    state = {start}
    while len(seen) <= cycles:
        twinkle = seen[len(seen) - 2]
        state = {
            p + s
            for p in state
            for s in [1, -1, 1j, -1j]
            if wrap(p + s) in graph
            if p + s not in twinkle
        }
        seen.append(twinkle | state)
    return seen


def extrapolate_quadratic(y0, y1, y2):
    a, b, c = (y2 - 2 * y1 + y0) / 2, (-y2 + 4 * y1 - 3 * y0) / 2, y0
    return lambda x: a * x ** 2 + b * x + c


text = open(0).read()
graph = {
    complex(x, y): val
    for y, row in enumerate(text.splitlines())
    for x, val in enumerate(row)
    if val in {'S', '.'}
}

width = max(int(p.real) for p in graph) + 1
height = max(int(p.imag) for p in graph) + 1
wrap = lambda p: complex(int(p.real % width), int(p.imag % height))

start, = (k for k, v in graph.items() if v == 'S')
seen = bfs_twinkle(start, graph, 327)
if width < 100:
    check = len({wrap(p) for p in seen[6]})
    print(check)
    exit()

ans1 = len({wrap(p) for p in seen[64]})
print(ans1)

goal = 26501365
size, = {height, width}
offset = goal % size

xs = [offset + size * i for i in range(3)]
ys = [len(seen[x]) for x in xs]
yf = extrapolate_quadratic(ys[0], ys[1], ys[2])

x = (goal - offset) / size
ans2 = int(yf(x))
print(ans2)
