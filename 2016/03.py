import re

with open('03.txt') as fp:
    grid = [[int(n) for n in line.split()] for line in fp]

ans = 0
g = iter(grid)
for box in zip(g,g,g):
    # box = zip(*box)
    for a,b,c in map(sorted,box):
        ans += a+b>c
print(ans)
