import sys
from math import prod


def slide(step):
    dx, dy = step
    seen, x, y = 0, 0, 0
    while y + dy < height:
        x += dx
        y += dy
        seen += grid[y][x % width] == '#'
    return seen


grid = sys.stdin.read().splitlines()
height = len(grid)
width = len(grid[0])

print(slide((3, 1)))
print(prod(map(slide, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])))
