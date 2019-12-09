import itertools
import re
import sys
from intcode import compute, parse


def check(noun, verb):
    ns = parse(text)
    ns[1] = noun
    ns[2] = verb
    list(compute(ns, 2))
    return ns[0]


text = sys.stdin.read()
print(check(12, 2))
for noun, verb in itertools.product(range(100), repeat=2):
    if check(noun, verb) == 19690720:
        print(100 * noun +  verb)
