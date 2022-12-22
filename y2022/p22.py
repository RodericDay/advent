import re


text = open(0).read()
p1, p2 = text.split('\n\n')

grid = {}
for y, row in enumerate(p1.splitlines()):
    for x, cell in enumerate(row):
        if cell.strip():
            grid[complex(x, y)] = cell


def render(grid):
    xmin, *_, xmax = sorted(int(p.real) for p in grid)
    ymin, *_, ymax = sorted(int(p.imag) for p in grid)
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            print(grid.get(complex(x, y), ' '), end='')
        print()


pos = min(grid, key=lambda p: (p.real == 0, p.imag))
grid[pos] = '@'
d = 1
for n, b in zip(map(int, re.sub(r'[A-Z]', ' ', p2).split()), re.sub(r'\d', ' ', p2).split()):
    for _ in range(n):
        if grid.get(pos + d) in set('.<v>^'):
            pos += d
        elif grid.get(pos + d) == '#':
            continue
        elif grid.get(pos + d) == None:
            lol = pos
            while grid.get(lol - d) != None:
                lol -= d
            if grid[lol] == '.':
                pos = lol
            else:
                continue
    d *= {'R': 1j, 'L': -1j}[b]


render(grid)
print(4 * int(pos.real + 1) + 1000 * int(pos.imag + 1) + {1: 0, -1j: 1, -1: 2, 1j: 3}[d])
