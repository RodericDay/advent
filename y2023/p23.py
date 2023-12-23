def move(old, seen, parents, special_rules):
    steps = [1, -1, 1j, -1j]
    for step in special_rules.get(graph[old], steps):
        new = old + step
        parents.setdefault(new, set()).add(old)
        if new in graph and new not in seen:
            yield new


def bfs(start, special_rules):
    parents = {}
    state = {start}
    seen = state.copy()
    while state:
        state = {new for old in state for new in move(old, seen, parents, special_rules)}
        seen |= state
    return parents


def segmentize(dense):
    sparse = {}
    for i, js in dense.items():
        for j in js:
            n = 1
            k = i
            while len(dense[j] - {k}) == 1:
                n += 1
                k, [j] = j, dense[j] - {k}
            sparse.setdefault(i, set()).add((j, n))
    return sparse


def recurse(pos, parents, path=set(), n=0):
    if pos == start:
        yield n
    else:
        for parent, cost in parents[pos]:
            if parent not in path:
                yield from recurse(parent, parents, path | {pos}, n + cost)


def solve(special_rules={}):
    dense = bfs(start, special_rules)
    sparse = segmentize(dense)
    return len(list(recurse(end, sparse)))


text = open(0).read()
graph = {
    complex(x, y): val
    for y, row in enumerate(text.splitlines())
    for x, val in enumerate(row)
    if val != '#'
}
start = min(graph, key=lambda p: (p.imag, p.real))
end = max(graph, key=lambda p: (p.imag, p.real))
print(solve({'<': [-1], '^': [-1j], 'v': [1j], '>': [1]}))
print(solve())
