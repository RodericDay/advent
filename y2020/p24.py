import collections
import re
import sys


def calc(pos):
    is_black = pos in active
    count = sum(pos + step in active for step in maps.values())
    if is_black and count not in {1, 2}:
        return False
    elif not is_black and count == 2:
        return True
    return is_black


text = sys.stdin.read()
maps = {'w': 2, 'e': -2, 'nw': 1+1j, 'ne': -1+1j, 'sw': 1-1j, 'se': -1-1j}
grid = collections.defaultdict(bool)
for line in text.splitlines():
    end = sum(map(maps.get, re.findall(r'(se|sw|nw|ne|e|w)', line)))
    grid[end] = not grid[end]
active = {pos for pos in grid if grid[pos]}
print(len(active))


for _ in range(100):
    active = {p + s for p in active for s in maps.values() if calc(p + s)}
print(len(active))
