import sys


grid = [line.split() for line in sys.stdin.readlines()]


ans1 = 0
for line in grid:
    a, b, c = sorted(map(int, line))
    ans1 += a + b > c
print(ans1)


ans2 = 0
for col in zip(*grid):
    for line in zip(*[iter(col)] * 3):
        a, b, c = sorted(map(int, line))
        ans2 += a + b > c
print(ans2)
