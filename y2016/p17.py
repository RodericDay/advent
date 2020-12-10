import sys

import toolkit


def advance(path, pos):
    digest = toolkit.md5(text + path)
    for d in [d for d, c in zip('UDLR', digest) if c in 'bcdef']:
        path1 = path + d
        new1 = pos + mapping[d]
        if 0 <= new1.real <= 3 and 0 <= new1.imag <= 3:
            yield path1, new1


text = sys.stdin.read().strip()
mapping = {'U': -1j, 'D': 1j, 'L': -1, 'R': 1}
edge = {('', 0)}
valid = []
while edge:
    edge = {new for old in edge for new in advance(*old)}
    valid += [new for new in edge if new[1] == 3 + 3j]
    edge -= set(valid)
print(valid[0][0])
print(len(valid[-1][0]))
