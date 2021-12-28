import itertools


def flash(k, flashed_this_round):
    state[k] = 0
    for p in (k + step for step in D8):
        if p in state and p not in flashed_this_round:
            state[p] += 1


state = {}
for y, line in enumerate(open(0)):
    for x, char in enumerate(line[:-1]):
        state[complex(x, y)] = int(char)
D8 = [dx + dy for dx in [1, 0, -1] for dy in [1j, 0, -1j] if dx + dy]

ans1 = 0
for i in itertools.count(1):
    for k in state:
        state[k] += 1

    flashed_this_round = set()
    while any(v > 9 for v in state.values()):
        for k, v in state.items():
            if v > 9:
                flash(k, flashed_this_round)
                flashed_this_round.add(k)

    if i <= 100:
        ans1 += len(flashed_this_round)

    if len({v for v in state.values()}) == 1:
        ans2 = i
        break
print(ans1)
print(ans2)
