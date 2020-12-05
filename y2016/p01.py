import re
import sys


pos = 0
ori = 1
seen = set()
ans2 = None
for turn, steps in re.findall(r'(R|L)(\d+)', sys.stdin.read()):
    ori *= {'R': 1j, 'L': -1j}[turn]
    for _ in range(int(steps)):
        pos += ori
        if ans2 is None and pos in seen:
            ans2 = abs(pos.real) + abs(pos.imag)
        seen.add(pos)
ans1 = abs(pos.real) + abs(pos.imag)
print(ans1)
print(ans2)
