text = open(0).read()
graph = {
    complex(x, y): val
    for y, row in enumerate(text.splitlines())
    for x, val in enumerate(row)
}
width = max(int(p.real) for p in graph) + 1
height = max(int(p.imag) for p in graph) + 1

wrap = lambda p: complex(p.real % width, p.imag % height)
start, = (k for k, v in graph.items() if v == 'S')
state = {(False, start)}
seen = state.copy()
for step in range(100):
    state = {
        (not age, p + s)
        for age, p in state
        for s in [1, -1, 1j, -1j]
        if graph[wrap(p + s)] in {'.', 'S'}
        if (not age, p + s) not in seen
    }
    seen |= state

    if step == 64:
        ans1 = sum(not age for age, pos in seen if pos in graph)
        print(ans1)

