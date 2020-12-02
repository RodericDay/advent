import sys
from itertools import combinations


ns = [int(n) for n in sys.stdin.read().splitlines()]


for a, b in combinations(ns, 2):
    if a + b == 2020:
        print(a * b)


for a, b, c in combinations(ns, 3):
    if a + b + c == 2020:
        print(a * b * c)
