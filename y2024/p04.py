inp = open(0).read().splitlines()

grid = {(x, y): cell for y, row in enumerate(inp) for x, cell in enumerate(row)}

ans1 = 0
ans2 = 0
for (x, y), cell in grid.items():
    if cell == 'X':
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if {dx, dy} != {0}:
                    try:
                        string = ''.join(grid[x + dx * i, y + dy * i] for i in range(4))
                        if string == 'XMAS':
                            ans1 += 1
                    except:
                        pass
    if cell == 'A':
        try:
            string1 = ''.join(grid[x + dx, y + dy] for dx, dy in [(-1, -1), (0, 0), (1, 1)])
            string2 = ''.join(grid[x + dx, y + dy] for dx, dy in [(1, -1), (0, 0), (-1, 1)])
            if {string1, string2} <= {'SAM', 'MAS'}:
                ans2 += 1
        except:
            pass
print(ans1)
print(ans2)
