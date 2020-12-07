import re
import sys


def display(state):
    ele, floors = state
    for i, floor in list(enumerate(floors))[::-1]:
        _ = ['E' if ele == i else ' ']
        _ += [d if d in floor else '..' for d in sorted(devices)]
        print(' '.join(_))
    print()


def checks(elevator, floors):
    for fl in floors:
        vulnerable = {d for d in fl if d == d.lower() and d.upper() not in fl}
        dangerous = {d for d in fl if d == d.upper()}
        if vulnerable and dangerous:
            yield False


def moves(ith, floors):
    for jth in {ith - 1, ith + 1} - {-1, 4}:
        for stuff in [{a, b} for a in floors[ith] for b in floors[ith]]:
            new = (jth, tuple(
                (floor | stuff) if ith == jth else (floor - stuff)
                for ith, floor in enumerate(floors)
            ))
            if all(checks(*new)):
                yield new


text = sys.stdin.read()
start = [
    frozenset(
        word[:2].upper() if not word.endswith('-') else word[:2]
        for word in re.findall(r'\w+ium-?', ln)
    )
    for ln in text.splitlines()
]
start[2] -= {'PR', 'RU', 'pr', 'ru'}
# start[0] |= {'EE', 'ee', 'DD', 'dd'}
devices = frozenset({device for floor in start for device in floor})

edge = {(0, tuple(start))}
goal = (3, tuple([frozenset(), frozenset(), frozenset(), devices]))
seen = {}
while goal not in seen:
    edge = {new: old for old in edge for new in moves(*old) if new not in seen}
    if not edge:
        raise RuntimeError('empty')
    seen = {**edge, **seen}
    print(len(edge))

seq = []
while goal != (0, tuple(start)):
    seq.append(goal)
    goal = seen[goal]
seq.append(goal)
seq.reverse()

for i, state in enumerate(seq):
    print(i)
    display(state)
