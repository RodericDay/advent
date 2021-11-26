import collections
import re
import sys


def read_in():
    grid = collections.defaultdict(lambda: ' ')
    for _ in data_file.read_text().splitlines():
        _ = _.replace(',', ';')
        _ = re.sub(r'(\d+)\.\.(\d+)', r'range(\1, \2 + 1)', _)
        _ = re.sub(r'=(\d+)', r'=[\1]', _)
        temp = {}
        exec(_, temp)
        grid.update({(X, Y): '#' for X in temp['x'] for Y in temp['y']})
    return grid


def flow(grid, start, ymax):
    stack = [start]
    while stack:
        x, y = stack.pop()
        grid[x, y] = '~'

        if y >= ymax:
            break

        for dx, dy in [(1, 0), (-1, 0), (0, 1)]:
            new = x + dx, y + dy
            if dy == 1 and grid[new] == '|':
                stack.clear()
                break

            if grid[new] == ' ':
                stack.append(new)

    drain(grid, (x, y), ymax)


def drain(grid, end, ymax):
    stack = [end]
    while stack:
        x, y = stack.pop()
        grid[x, y] = '|'

        left, right, below = grid[x - 1, y], grid[x + 1, y], grid[x, y + 1]
        if all([right == ' ', left == '|', below != '|']):
            flow(grid, (x + 1, y), ymax)

        for dx, dy in [(-1, 0), (1, 0), (0, -1)]:
            new = x + dx, y + dy
            if grid[new] == '~':
                stack.append(new)


grid = read_in()
ymin, *_, ymax = sorted(y for x, y in grid if grid[x, y] == '#')
flow(grid, (500, ymin), ymax)
counter = collections.Counter(grid.values())
ans1 = counter['~'] + counter['|']
ans2 = counter['~']
