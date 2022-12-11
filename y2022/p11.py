import functools
import operator
import re


class Monkey:

    def __init__(self, description):
        relevant = re.findall(r'\d+|old|\*|\+', description)
        parsed = [int(n) if n.isdigit() else n for n in relevant]
        self.idx, *self.items, _, op, op_arg, self.div, aa, bb = parsed
        op = {'*': operator.mul, '+': operator.add}[op]
        self.fn = lambda x: op(x, x if op_arg == 'old' else op_arg)
        self.target = lambda x: aa if x % self.div == 0 else bb

    def __repr__(self):
        return f'Monkey_{self.idx}({self.items})'


def play(monkeys, n_rounds, act):
    counts = [0 for _ in monkeys]
    for _ in range(n_rounds):
        for monkey in monkeys:
            while monkey.items:
                counts[monkey.idx] += 1
                item = act(monkey, monkey.items.pop())
                monkeys[monkey.target(item)].items.append(item)
    yy, zz = sorted(counts)[-2:]
    return yy * zz


text = open(0).read()

monkeys = [Monkey(descr) for descr in text.strip().split('\n\n')]
ans1 = play(monkeys, 20, lambda m, i: int(m.fn(i) / 3))
print(ans1)

monkeys = [Monkey(descr) for descr in text.strip().split('\n\n')]
lim = functools.reduce(operator.mul, [m.div for m in monkeys])
ans2 = play(monkeys, 10_000, lambda m, i: m.fn(i) % lim)
print(ans2)
