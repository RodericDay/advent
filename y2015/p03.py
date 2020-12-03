import sys
from itertools import accumulate as acc


text = sys.stdin.read()
dirs = dict(zip('<>^v', [-1, 1, -1j, 1j]))

ans1 = len({*acc(map(dirs.get, text))})
print(ans1)

ans2 = len({*acc(map(dirs.get, text[::2])), *acc(map(dirs.get, text[1::2]))})
print(ans2)
