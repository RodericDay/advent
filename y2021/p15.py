import heapq


def shortest_path(graph, X, Y):
    risk = {0: 0}
    seen = set()
    heap = [(0, '', 0)]  # string disambiguates cost ties for imaginary numbers

    end = complex(X - 1, Y - 1)
    tip = 0
    while end not in seen:
        _, _, tip = heapq.heappop(heap)
        seen.add(tip)
        for y in (tip + dx for dx in [1, -1, 1j, -1j]):
            if y in graph:
                if y not in risk or risk[y] > graph[y] + risk[tip]:
                    risk[y] = graph[y] + risk[tip]
                    heapq.heappush(heap, (risk[y], str(y), y))

    return risk[end]


graph = {}
for y, line in enumerate(text.splitlines()):
    for x, char in enumerate(line):
        graph[complex(x, y)] = int(char)
X, Y = x + 1, y + 1

ans1 = shortest_path(graph, X, Y)

graph = {
    pos + complex(X * dx, Y * dy): sum(divmod(graph[pos] + dx + dy, 10))
    for pos, value in graph.items()
    for dx in range(5)
    for dy in range(5)
}
ans2 = shortest_path(graph, 5 * X, 5 * Y)
