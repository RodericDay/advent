import re
import sys


def freeze(state):
    return tuple(frozenset(fl) for fl in state)


def thaw(state):
    return [set(fl) for fl in state]


def checks(state):
    for fl in state:
        dangerous = {d[:-1] for d in fl if d.endswith('+')}
        vulnerable = {d[:-1] for d in fl if d.endswith('-')} - dangerous
        if dangerous and vulnerable:
            yield False


def advance(pair):
    f0, state = pair
    for devices in {frozenset({a, b}) for a in state[f0] for b in state[f0]}:
        for f1 in {f0 + 1, f0 - 1} - {-1, 4}:
            if len(devices) == 1 or f1 > f0:
                new = thaw(state)
                new[f0] -= devices
                new[f1] |= devices
                if all(checks(new)):
                    yield f1, freeze(new)


text = sys.stdin.read()
state = [
    {a + (b or '+') for a, b in re.findall(r'(\w{2})\w+ium(-)?', ln)}
    for ln in text.splitlines()
]

goal = (3, freeze([{}, {}, {}, {d for fl in state for d in fl}]))
edge = {(0, freeze(state))}
seen = set()
ans1 = 0
while goal not in seen:
    edge = {new for old in edge for new in advance(old)} - seen
    seen |= edge
    ans1 += 1
print(ans1)
print(ans1 + 12 * 2)
