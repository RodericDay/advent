import operator
import re
from collections import namedtuple
from math import prod


def make_monkey(description):
    relevant = re.findall(r'\d+|old|\*|\+', description)
    parsed = [int(n) if n.isdigit() else n for n in relevant]
    _, *items, _, op, y, div, aa, bb = parsed

    op = {'*': operator.mul, '+': operator.add}[op]
    grow_item = lambda x: op(x, x if y == 'old' else y)
    find_target = lambda x: aa if x % div == 0 else bb
    return Monkey(items, grow_item, find_target)


def play(monkeys, n_rounds, shrink):
    counts = [0 for _ in monkeys]
    for _ in range(n_rounds):
        for idx, monkey in enumerate(monkeys):
            while monkey.items:
                counts[idx] += 1
                item = monkey.items.pop()
                item = monkey.grow_item(item)
                item = shrink(item)
                idx = monkey.find_target(item)
                monkeys[idx].items.append(item)
    return prod(sorted(counts)[-2:])


text = open(0).read()
Monkey = namedtuple('Monkey', ['items', 'grow_item', 'find_target'])

monkeys = [make_monkey(descr) for descr in text.strip().split('\n\n')]
ans1 = play(monkeys, 20, lambda x: x // 3)
print(ans1)

lim = prod(map(int, re.findall(r'divisible by (\d+)', text)))
monkeys = [make_monkey(descr) for descr in text.strip().split('\n\n')]
ans2 = play(monkeys, 10_000, lambda x: x % lim)
print(ans2)
