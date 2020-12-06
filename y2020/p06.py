import functools
import sys


text = sys.stdin.read().strip()

ans1 = 0
ans2 = 0
for blob in text.split('\n\n'):
    ans1 += len(set(blob) - {'\n'})

    anses = [set(stuff) for stuff in blob.split('\n')]
    ans2 += len(functools.reduce(lambda a, b: a & b, anses))
print(ans1)
print(ans2)
