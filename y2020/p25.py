import itertools
import sys


text = sys.stdin.read()
A, B = map(int, text.splitlines())

val = 1
subj = 7
for i in itertools.count():
    val = (val * subj) % 20201227
    if val == A:
        loopA = i + 1
        break

val = 1
subj = B
for _ in range(loopA):
    val = (val * subj) % 20201227
print(val)
