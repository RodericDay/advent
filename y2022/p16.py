import collections
import itertools
import re

text = open(0).read()


graph = collections.defaultdict(dict)
rates = {}
for ln in text.splitlines():
    source, rate, *leads_to = re.findall(r'[A-Z]{2}|\d+', ln)
    for out in leads_to:
        graph[out][source] = 1
        graph[source][out] = 1
    rates[source] = int(rate)


costs = {}
for k in graph:
    edge = set(graph[k])
    seen = set()
    cost = 1
    while True:
        for e in edge:
            if (k, e) in costs:
                costs[k, e] = min(costs[k, e], cost)
            else:
                costs[k, e] = cost
        cost += 1
        edge = {n for e in edge for n in graph[e]} - seen
        if seen == set(graph):
            break
        seen |= edge


def for_one(combo, lim):
    tt = 0
    bob = [0]
    for a, b in zip(('AA',) + combo, combo):
        tt = costs[a, b]
        for _ in range(tt):
            bob.append(bob[-1])
        bob.append(bob[-1] + rates[b])
    pending = max(0, lim - len(bob))
    bob += [bob[-1]] * pending
    return sum(bob[:lim])


def generate_combos(pending, left, carry=('AA',)):
    if left < 0 or not pending:
        yield carry[1:]
    else:
        for k in pending:
            yield from generate_combos(pending - {k}, left - costs[carry[-1], k], carry + (k,))


combos = generate_combos({k for k, v in rates.items() if v}, lim=30)
best = max(combos, key=for_one)
print(best)
print(for_one(best))
# 2615
