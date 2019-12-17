import re
import sys

from intcode import compute, parse

from toolkit import read_image


# part1
text = sys.stdin.read()
snapshot = ''.join(chr(val) for val in compute(text, 0))
grid = read_image(snapshot)
alignment_parameters = [
    (pos.real, pos.imag)
    for pos, val in grid.items()
    if {grid.get(pos + d) for d in [0, 1, -1, 1j, -1j]} == {'#'}
]
print(int(sum(a * b for a, b in alignment_parameters)))

# find path
pos = {v: k for k, v in grid.items()}['^']
ori = -1j
path = []
while {grid[pos + ori * rot] for rot in [1, 1j, -1j]} != {'.'}:
    if grid[pos + ori] == '#':
        pos += ori
        path[-1] += 1
    else:
        for c, rot in [('R', 1j), ('L', -1j)]:
            if grid[pos + ori * rot] == '#':
                ori *= rot
                path += [c, 0]
full_path = ','.join(str(c) for c in path) + ','

# compress
regex = r'^(.{2,21})(?:\1)*(.{2,21})(?:\1|\2)*(.{2,21})(?:\1|\2|\3)*$'
A, B, C = [group.strip(',') for group in re.match(regex, full_path).groups()]
MAIN = full_path.replace(A, 'A').replace(B, 'B').replace(C, 'C').strip(',')

# part2
mem = parse(text)
mem[0] += 1
code = ('\n'.join([MAIN, A, B, C, 'n']) + '\n').encode()
output = ''.join(chr(val) for val in compute(mem, iter(code)))
print(ord(output[-1]))
