import re


order = ['ore', 'clay', 'obsidian', 'geode']
blueprints = []
for ln in open(0).read().split('Blueprint')[1:]:
    costs = []
    for ln in [re.findall(r'(\d+) (\w+)', part) for part in ln.split('Each')[1:]]:
        cost = [0, 0, 0, 0]
        for qty, kind in ln:
            cost[order.index(kind)] = int(qty)
        costs.append(tuple(cost))
    blueprints.append(tuple(costs))


def evolve(bots, ores, choice, blueprint, lims):
    if all(o >= b for o, b in zip(ores, blueprint[3])) and choice != 3:
        return

    if choice != -1:
        ores = tuple(a - b for a, b in zip(ores, blueprint[choice]))
        if any(a < 0 for a in ores):
            return

    ores = tuple(a + b for a, b in zip(ores, bots))

    if choice != -1:
        bots = tuple(a + (choice == i) for i, a in enumerate(bots))

    if any(q > l for q, l in zip(bots, lims[:-1])):
        return

    yield (bots, ores)


def solve(blueprint):
    states = {((1, 0, 0, 0), (0, 0, 0, 0))}
    lims = list(map(max, zip(*blueprint)))
    for _ in range(24):
        print('.', end='')
        states = {new for old in states for choice in [-1, 0, 1, 2, 3] for new in evolve(*old, choice, blueprint, lims)}
        best = max(s[0][-1] for s in states)
        states = {s for s in states if best - s[0][-1] < 2}
    print()
    return max(states, key=lambda state: state[-1][-1])


ans1 = 0
ans2 = 1
for idx, bp in enumerate(blueprints, 1):
    state = solve(bp)
    ans1 += idx * state[-1][-1]
    ans2 *= state[-1][-1]
    print(idx, ans1, state[-1][-1])
print(ans1)
print(ans2)
