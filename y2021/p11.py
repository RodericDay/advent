import itertools
import toolkit


state = {k: int(v) for k, v in toolkit.read_image(text)[0].items()}
D8 = [dx + dy for dx in [1, 0, -1] for dy in [1j, 0, -1j] if dx + dy]


def flash(k, flashed_this_round):
    state[k] = 0
    for p in (k + step for step in D8):
        if p in state and p not in flashed_this_round:
            state[p] += 1


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
