steps = {
    'n': (1, 0),
    's': (-1, 0),
    'ne': (0.5, 0.5),
    'se': (-0.5, 0.5),
    'nw': (0.5, -0.5),
    'sw': (-0.5, -0.5),
}
x, y = 0, 0
ans2 = 0
for dx, dy in map(steps.get, data_file.read_text().strip().split(',')):
    x, y = x + dx, y + dy
    dist = int(abs(x) + abs(y))
    ans2 = max(ans2, dist)
ans1 = dist
