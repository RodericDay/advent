import heapq


def shortest_path(graph, start, end):
    risk_sum = {start: 0}
    heap = [(0, *start)]
    while end not in risk_sum:
        risk, x, y = heapq.heappop(heap)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            adj = (x + dx, y + dy)
            if adj in graph:
                if adj not in risk_sum or risk_sum[adj] > graph[adj] + risk:
                    risk_sum[adj] = graph[adj] + risk
                    heapq.heappush(heap, (risk_sum[adj], x + dx, y + dy))
    return risk_sum[end]


graph = {}
for y, line in enumerate(open(0).read().splitlines()):
    for x, char in enumerate(line):
        graph[x, y] = int(char)
X, Y = x + 1, y + 1

ans1 = shortest_path(graph, min(graph), max(graph))
print(ans1)

graph = {
    (x + X * dx, y + Y * dy): sum(divmod(graph[x, y] + dx + dy, 10))
    for (x, y), value in graph.items()
    for dx in range(5)
    for dy in range(5)
}
ans2 = shortest_path(graph, min(graph), max(graph))
print(ans2)
