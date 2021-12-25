text = open(0).read()
state = {}
for y, row in enumerate(text.splitlines()):
    for x, ch in enumerate(row):
        state[x, y] = ch
X, Y = x + 1, y + 1

seen = set()
for turn in range(1000):
    for ch, dx, dy in [('>', 1, 0), ('v', 0, 1)]:
        copy = state.copy()
        for old in copy:
            if copy[old] == ch:
                x, y = old
                new = (x + dx) % X, (y + dy) % Y
                if copy[new] == '.':
                    state[old] = '.'
                    state[new] = ch

    hashable = frozenset(state.items())
    if hashable in seen:
        print(turn)
        break
    seen.add(hashable)
