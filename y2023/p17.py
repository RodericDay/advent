import random
import heapq


def solve(ns):
    heap = [(0, None, 0, d) for d in [1, 1j]]
    exhausted = set()
    while True:
        old_cost, _, old_pos, old_dir = heapq.heappop(heap)

        if old_pos == end:
            break

        key = old_pos, old_dir
        if key in exhausted:
            continue
        exhausted.add(key)

        for n in ns:
            new_pos = old_pos + old_dir * n
            if new_pos not in graph:
                break
            new_cost = old_cost + sum(graph[old_pos + i * old_dir] for i in range(1, n + 1))

            heapq.heappush(heap, (new_cost, random.random(), new_pos, old_dir * 1j))
            heapq.heappush(heap, (new_cost, random.random(), new_pos, old_dir / 1j))
    return old_cost


text = open(0).read()
graph = {
    complex(x, y): int(val)
    for y, row in enumerate(text.splitlines())
    for x, val in enumerate(row)
}
xmax = max(int(p.real) for p in graph)
ymax = max(int(p.imag) for p in graph)
end = complex(xmax, ymax)
print(solve([1, 2, 3]))
print(solve(list(range(4, 11))))
