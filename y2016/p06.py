import sys
from collections import Counter


grid = sys.stdin.read().splitlines()
transpose = list(zip(*grid))

ans1 = ''.join(Counter(line).most_common()[0][0] for line in transpose)
print(ans1)

ans2 = ''.join(Counter(line).most_common()[-1][0] for line in transpose)
print(ans2)
