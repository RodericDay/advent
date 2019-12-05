import collections
import re
from pathlib import Path


def read_in():
    grid = collections.defaultdict(lambda: ' ')
    for _ in Path('y2018/p17.dat').read_text().splitlines():
        _ = _.replace(',', ';')
        _ = re.sub(r'(\d+)\.\.(\d+)', r'range(\1, \2 + 1)', _)
        _ = re.sub(r'=(\d+)', r'=[\1]', _)
        exec(_, globals())
        grid.update({(X, Y): '#' for X in x for Y in y})
    return grid


def write_out(grid, path):
    text = '\n'.join(
        ''.join(grid[x, y] for x in range(xmin - 5, xmax + 5))
        for y in range(ymin, ymax + 1)
    )
    Path(path).write_text(text)


def flow(start):
    stack = [start]
    while stack:
        x, y = stack.pop()
        grid[x, y] = '~'

        if y > ymax:
            break

        for dx, dy in [(1, 0), (-1, 0), (0, 1)]:
            new = x + dx, y + dy
            if dy == 1 and grid[new] == '|':
                stack.clear()
                break

            if grid[new] == ' ':
                stack.append(new)

    drain((x, y))


def drain(end):
    stack = [end]
    while stack:
        x, y = stack.pop()
        grid[x, y] = '|'

        if grid[x - 1, y] == '|' and grid[x + 1, y] == ' ' and grid[x, y + 1] != '|':
            flow((x + 1, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1)]:
            new = x + dx, y + dy
            if grid[new] == '~':
                stack.append(new)


grid = read_in()
xmin, *_, xmax = sorted(x for x, y in grid)
ymin, *_, ymax = sorted(y for x, y in grid)
flow((500, 0))
counter = collections.Counter(grid.values())
print(counter['~'] + counter['|'])
print(counter['~'])
write_out(grid, 'y2018/p17out.dat')
