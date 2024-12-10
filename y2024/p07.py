import re
import math
import itertools
import functools
import operator


def solve(ops):
    for ln in inp.splitlines():
        n, *ns = map(int, re.findall(r'\d+', ln))
        for seq in itertools.product(ops, repeat=len(ns) - 1):
            if n == functools.reduce(lambda a, b: b[0](a, b[1]), zip(seq, ns[1:]), ns[0]):
                yield n
                break


inp = open(0).read()

ops = [operator.add, operator.mul]
print(sum(solve(ops)))

# concat = lambda a, b: int(f'{a}{b}')
concat = lambda a, b: a * 10 ** math.ceil(math.log10(b + 1)) + b
print(sum(solve(ops + [concat])))
