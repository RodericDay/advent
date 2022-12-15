import collections
import re

text = open(0).read()
grid = {}
match = {}
for x, y, a, b in [[int(n) for n in re.findall(r'-?\d+', ln)] for ln in text.splitlines()]:
    match[complex(x, y)] = complex(a, b)

goal = 2000000
bop = 4000000
seen = set()
count = collections.Counter()
for aa, bb in match.items():
    diff = bb - aa
    reach = int(abs(diff.real) + abs(diff.imag))
    dist = int(abs(aa.imag - goal))
    if reach > dist:
        df = reach - dist
        seen |= set(range(int(aa.real - df), int(aa.real + df)))

    for rot in [1j ** i for i in range(4)]:
        for dx in range(reach):
            dy = reach - dx
            edgy = aa + complex(dx, dy) * rot
            for dot in [rot, rot * 1j]:
                bip = edgy + dot
                if 0 <= bip.real <= bop and 0 <= bip.imag <= bop:
                    count[bip] += 1

print(len(seen))
fin = count.most_common()[0][0]
print(fin, int(fin.real * bop + fin.imag))
