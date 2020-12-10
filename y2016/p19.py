import collections
import sys


text = sys.stdin.read()
lim = int(text) + 1

elves = collections.deque(range(1, lim + 1))
while len(elves) > 1:
    elves.rotate(-1)
    elves.popleft()
print(elves[0])

half1 = collections.deque(range(1, lim // 2 + 1))
half2 = collections.deque(range(lim // 2 + 1, lim + 1))
while half1 and half2:
    half1.pop() if len(half2) < len(half1) else half2.popleft()
    half2.append(half1.popleft())
    half1.append(half2.popleft())
print([*half1, *half2][0])
