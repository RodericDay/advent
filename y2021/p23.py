from functools import lru_cache


@lru_cache(maxsize=None)
def find_min_dist(valid, a, b, DX=[1, -1, 1j, -1j]):
    dist = 0
    state = {a}
    seen = state.copy()
    while state:
        dist += 1
        state = {x + dx for x in state for dx in DX} & valid - seen
        seen.update(state)
        if b in state:
            return dist


def evolve(old, pinned):
    valid = frozenset({p for p, c in old if c == '.'})
    for x, k in old:
        if x not in pinned and k.isalpha():
            xi = 'ABCD'.index(k) * 2 + 3
            cost = 10 ** 'ABCD'.index(k)

            # rule: if you're in the hall, you can only end up in your room
            if x.imag == 1:
                ys = {complex(xi, y) for y in slots}
            # rule: if you're in a wrong spot, you can only end up in the hall
            else:
                ys = {complex(x, 1) for x in (1, 2, 4, 6, 8, 10, 11)}

            for y in ys & valid:
                # heuristic: assume only A can waste time with alcove
                if y.real in {1, 2} and k != 'A':
                    continue

                # rule: you only get one move
                new_pinned = pinned
                if y.imag > 1:
                    new_pinned |= {y}

                if dist := find_min_dist(valid, x, y):
                    new = old - {(x, k), (y, '.')} | {(x, '.'), (y, k)}
                    options = {scores.get(new), scores[old] + cost * dist}
                    scores[new] = min(options - {None})
                    yield new, new_pinned


text = open(0).read()
expansion = '''
  #D#C#B#A#
  #D#B#A#C#
'''
expanded_text = text.replace('#\n ', '#' + expansion + ' ', 1)
for text in [text, expanded_text]:
    slots = list(range(2, len(text.splitlines()) - 1))
    init = frozenset(
        (complex(x, y), ch)
        for y, ln in enumerate(text.splitlines())
        for x, ch in enumerate(ln)
    )
    goal = {
        (complex(i * 2 + 3, y), ch)
        for i, ch in enumerate('ABCD')
        for y in slots
    }
    scores = {init: 0}
    states = {(init, frozenset())}
    wins = set()
    seen = set()
    i = 0
    while states:
        i += 1; print(i, len(states))
        states = {new for old in states for new in evolve(*old)} - seen
        seen |= states
        if wins := {old[0] for old in states if goal < old[0]}:
            print('end', scores[min(wins, key=scores.get)])
            break
