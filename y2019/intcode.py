import collections
import itertools
import re


MODES = {
    '0': lambda ns, x, relbase: ns[x],
    '1': lambda ns, x, relbase: x,
    '2': lambda ns, x, relbase: ns[x + relbase],
    '0-special': lambda ns, x, relbase: x,
    '2-special': lambda ns, x, relbase: x + relbase,
}


def get_parameters(ns, pos, modes, N, writes, relbase):
    for c in writes:
        # paradox: return immediate mode to use positionally outside
        modes[ord(c) - ord('a')] += '-special'

    yield pos + N
    for i in range(N):
        mode, x = modes[i], ns[pos + i]
        yield MODES[mode](ns, x, relbase)


def compute(ns, in_iter):
    def consume(N, writes=''):
        return get_parameters(ns, pos, modes, N, writes, relbase)

    if isinstance(ns, str):
        ns = parse(ns)
    if isinstance(in_iter, int):
        in_iter = itertools.cycle([in_iter])

    pos = 0
    relbase = 0

    while True:
        op = ns[pos] % 100
        # instructions stupidly say ABC referring to parameters 3, 2, 1
        # we do a, b, c
        modes = list(str(ns[pos] // 100)[::-1] + '000')
        pos += 1

        if op == 1:
            pos, a, b, c = consume(3, 'c')
            ns[c] = a + b

        elif op == 2:
            pos, a, b, c = consume(3, 'c')
            ns[c] = a * b

        elif op == 3:
            pos, a = consume(1, 'a')
            ns[a] = next(in_iter)

        elif op == 4:
            pos, a = consume(1)
            yield a

        elif op == 5:
            pos, a, b = consume(2)
            if a != 0:
                pos = b

        elif op == 6:
            pos, a, b = consume(2)
            if a == 0:
                pos = b

        elif op == 7:
            pos, a, b, c = consume(3, 'c')
            ns[c] = int(a < b)

        elif op == 8:
            pos, a, b, c = consume(3, 'c')
            ns[c] = int(a == b)

        elif op == 9:
            pos, a = consume(1)
            relbase += a

        elif op == 99:
            return

        else:
            raise RuntimeError(op)


def parse(string):
    ns = [int(n) for n in re.findall(r'-?\d+', string)]
    memory = collections.defaultdict(int)
    memory.update(enumerate(ns))
    return memory
