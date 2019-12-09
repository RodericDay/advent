import collections
import itertools
import re


def parse(string):
    memory = collections.defaultdict(int)
    memory.update(enumerate(int(n) for n in re.findall(r'-?\d+', string)))
    return dict(memory)


def get_parameters(ns, pos, modes, N, writes, relbase):
    for c in writes:
        # paradox: return immediate mode to use positionally outside
        modes[ord(c) - ord('a')] += '-special'

    for mode, x in zip(modes, [ns[y] for y in range(pos, pos + N)]):
        yield {
            '0': lambda: ns[x],
            '1': lambda: x,
            '2': lambda: ns[x + relbase],
            '0-special': lambda: x,
            '2-special': lambda: x + relbase,
        }[mode]()

    yield pos + N


def compute(ns, in_iter):
    if isinstance(ns, str):
        ns = parse(ns)
    if isinstance(in_iter, int):
        in_iter = itertools.cycle([in_iter])

    pos = 0
    relbase = 0
    consume = lambda n, writes='': get_parameters(ns, pos, modes, n, writes, relbase)

    while True:
        op = ns[pos] % 100
        # instructions stupidly say ABC referring to parameters 3, 2, 1
        # we do a, b, c
        modes = list(str(ns[pos] // 100).zfill(3)[::-1])
        pos += 1

        if op == 1:
            a, b, c, pos = consume(3, 'c')
            ns[c] = a + b

        elif op == 2:
            a, b, c, pos = consume(3, 'c')
            ns[c] = a * b

        elif op == 3:
            a, pos = consume(1, 'a')
            ns[a] = next(in_iter)

        elif op == 4:
            a, pos = consume(1)
            yield a

        elif op == 5:
            a, b, pos = consume(2)
            if a != 0:
                pos = b

        elif op == 6:
            a, b, pos = consume(2)
            if a == 0:
                pos = b

        elif op == 7:
            a, b, c, pos = consume(3, 'c')
            ns[c] = int(a < b)

        elif op == 8:
            a, b, c, pos = consume(3, 'c')
            ns[c] = int(a == b)

        elif op == 9:
            a, pos = consume(1)
            relbase += a

        elif op == 99:
            return

        else:
            raise RuntimeError(op)
