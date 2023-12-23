"""
5000 steps, he can reach 16733044 garden plots.

26501365?
"""
text = open(0).read()
graph = {
    complex(x, y): val
    for y, row in enumerate(text.splitlines())
    for x, val in enumerate(row)
}

width = max(int(p.real) for p in graph) + 1
height = max(int(p.imag) for p in graph) + 1
block = lambda p: complex(p.real // width, p.imag // height)
wrap = lambda p: complex(p.real % width, p.imag % height)

start, = (k for k, v in graph.items() if v == 'S')
seen = [set(), set()]
state = {start}
bops = set()
for step in range(130):
    twinkle = seen[step % 2]
    twinkle |= state

    if step == 64:
        print(len(twinkle))  # ans1

    state = {
        p + s
        for p in state
        for s in [1, -1, 1j, -1j]
        if graph[wrap(p + s)] in {'.', 'S'}
        if p + s not in twinkle
    }
