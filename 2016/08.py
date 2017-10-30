import re
from collections import deque

def create(w, h):
    return [list(' '*w) for _ in range(h)]

def display(grid):
    print('\n'.join(''.join(row) for row in grid)+'\n')

def rect(data):
    w, h = map(int, data.split('x'))
    for i in range(h):
        for j in range(w):
            grid[i][:w] = list('#'*w)

def rotate(data):
    global grid
    what, data = data.split(' ', 1)
    i, n = map(int, re.findall(r'\d+', data))
    if what=='column': grid = list(map(list,zip(*grid)))
    row = deque(grid[i])
    row.rotate(n)
    grid[i] = list(row)
    if what=='column': grid = list(map(list,zip(*grid)))


grid = create(50, 6)
with open('08.txt') as fp:
    for line in fp.read().splitlines():
        inst, data = line.split(' ', 1)
        eval(inst)(data)
display(grid)
print(''.join(''.join(row) for row in grid).count('#'))
