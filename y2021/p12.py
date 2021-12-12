from collections import defaultdict, Counter


def solve(graph, part2=False):
    edge = [('start',)]
    final = []
    while edge:
        edge = [
            route + (new,)
            for route in edge
            for new in graph[route[-1]]
            if new.isupper() or route.count(new) == 0
            or part2 & (
                new != 'start'
                and route.count(new) == 1
                and max(Counter(filter(str.islower, route)).values()) == 1
            )
        ]
        final.extend(el for el in edge if el[-1] == 'end')
        edge = [el for el in edge if el[-1] != 'end']
    return len(final)


graph = defaultdict(set)
for ln in text.splitlines():
    a, b = ln.split('-')
    graph[a].add(b)
    graph[b].add(a)
graph = dict(graph)
ans1 = solve(graph)
ans2 = solve(graph, True)
