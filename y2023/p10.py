def around(x, graph, adj):
    if x in graph:
        for dx in adj[graph[x]]:
            y = x + dx
            if x in {y + dy for dy in adj[graph[y]]}:
                yield y
                yield x + (y - x) / 2 # this extends the pipeline to include mid-joints


text = open(0).read()
graph = {complex(x, y): val
    for y, row in enumerate(text.splitlines())
    for x, val in enumerate(row)
}
adj = {
    'S': [1, -1, 1j, -1j],
    '-': [1, -1],
    '.': [],
    '|': [1j, -1j],
    'L': [1, -1j],
    '7': [1j, -1],
    'J': [-1j, -1],
    'F': [1j, 1],
}
state = {k for k in graph if graph[k] == 'S'}
seen = {}
n = 0
while state:
    seen |= {k: n for k in state}
    state = {y for x in state for y in around(x, graph, adj) if y not in seen}
    n += 1
print(max(seen.values()))


def connected(nodes, steps):
    while nodes:
        edge = {nodes.pop()}
        seen = edge.copy()
        while edge:
            edge = {node + step for node in edge for step in steps} & nodes - seen
            seen |= edge
        nodes -= seen
        yield seen


steps = {(dx + dy) / 2 for node in graph for dx in [-1, 0, 1] for dy in [-1j, 0, 1j]}
nodes = {node + step for node in graph for step in steps} - set(seen)
print(sum(len(group & set(graph)) for group in connected(nodes, steps) if not 0 in group))
