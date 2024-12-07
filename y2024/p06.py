inp = open(0).read()

grid = {complex(x, y): cell for y, row in enumerate(inp.splitlines()) for x, cell in enumerate(row)}

start = {v: k for k, v in grid.items()}['^']
grid[start] = '.'

def render(grid):
    W = max(int(p.real) for p in grid) + 1
    H = max(int(p.imag) for p in grid) + 1
    print('\n'.join(''.join(grid[complex(x, y)] for x in range(W)) for y in range(H)) + '\n')

def run(grid):
    aim = -1j
    pos = start
    seen = {(pos, aim)}
    while pos in grid:
        if pos + aim not in grid:
            break  # broke free

        if grid.get(pos + aim) == '.':
            pos += aim
        else:
            aim *= 1j
            continue

        if (pos, aim) in seen:
            # render(grid | {p: '@' for p, a in seen})
            return False  # stuck in loop

        seen.add((pos, aim))
    seen.add((pos, aim))
    return len({pos for pos, aim in seen})

print(run(grid))

W = max(int(p.real) for p in grid) + 1
H = max(int(p.imag) for p in grid) + 1
print(sum(not run(dict(grid) | {complex(x, y): 'O'}) for y in range(H) for x in range(W) if grid[complex(x, y)] == '.'))
