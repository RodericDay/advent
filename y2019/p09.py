import sys

from intcode import compute


text = sys.stdin.read()
print(next(compute(text, 1)))
print(next(compute(text, 2)))
