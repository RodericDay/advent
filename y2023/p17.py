text = open(0).read()
graph = {
    complex(x, y): int({'.': 1, '#': 10000}.get(val, val))
    for y, row in enumerate(text.splitlines())
    for x, val in enumerate(row)
}
xmax = max(int(p.real) for p in graph)
ymax = max(int(p.imag) for p in graph)
end = complex(xmax, ymax)
mapping = {1: '>', -1: '<', 1j: 'v', -1j: '^'}

# a position mapped to the lowest effort taken to reach it
edge = {(0, ''): (0, '')}
exhausted = {}
while end not in exhausted:
    pos = min(edge, key=edge.get)
    parent = edge.pop(pos)
    if pos[0] == end:
        break
    exhausted[pos] = parent
    for step in [1, -1, 1j, -1j]:
        # no reverse
        if pos[1] and pos[1][-1] == mapping[-step]: continue

        # turn condition
        bop = pos[1] + mapping[step]
        if len(bop) == 4 and len(set(bop)) == 1: continue

        adj = pos[0] + step, bop[-3:]

        # out of bounds check
        if adj[0] not in graph: continue

        # some positions are truly dead
        if adj in exhausted: continue

        score = parent[0] + graph[adj[0]], parent[1] + mapping[step]
        if adj not in edge:
            edge[adj] = score
        else:
            edge[adj] = min(edge[adj], score)


def scorer(seq):
    pos = 0
    out = 0
    for char in seq:
        pos += {'>': 1, '<': -1, '^': -1j, 'v': 1j}[char]
        out += graph[pos]
    return out


print(parent[1], scorer(parent[1]))
test = '>>>v>>>^>>>vv>vv>vvv>vvv<vv>'
print(test, scorer(test))
