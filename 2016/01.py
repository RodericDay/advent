import re

with open('01.txt') as fp:
    txt = fp.read()

angle = 1j
position = 0
seen = set()
overlap = None

for spin, step in re.findall(r'(L|R)(\d+)', txt):
    angle *= {'L':+1j,'R':-1j}[spin]
    for i in range(int(step)):
        position += angle
        if not overlap and position in seen:
            overlap = position
        else:
            seen.add(position)

print(position)
print(overlap)
