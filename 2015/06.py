import re

with open('06.txt') as fp:
    txt = fp.read()

def calculate(fn):
    X, Y = 1000, 1000
    grid = [[False for _ in range(X)] for _ in range(Y)]

    pattern = r'(on|off|toggle) (\d+),(\d+) through (\d+),(\d+)'
    for action, *n in re.findall(pattern, txt):
        x1, y1, x2, y2 = map(int, n)

        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                grid[y][x] = fn[action](grid[y][x])

    return grid

fn1 = {
    'off': lambda state: False,
    'on': lambda state: True,
    'toggle': lambda state: not state,
}
ans1 = sum(v for row in calculate(fn1) for v in row)
print(ans1)

fn2 = {
    'off': lambda state: max(state-1, 0),
    'on': lambda state: state+1,
    'toggle': lambda state: state+2,
}
ans2 = sum(v for row in calculate(fn2) for v in row)
print(ans2)
