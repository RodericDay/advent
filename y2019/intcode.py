import re


def parse(string):
    return [int(n) for n in re.findall(r'-?\d+', string)]


def get_parameters(ns, pos, modes, N, writes):
    for c in writes:
        # paradox: return immediate mode to use positionally outside
        modes[ord(c) - ord('a')] = '1'

    for mode, x in zip(modes, ns[pos:][:N]):
        yield {
            '0': lambda: ns[x],
            '1': lambda: x,
        }[mode]()

    yield pos + N


def compute(ns, inp):
    if isinstance(ns, str):
        ns = parse(ns)

    pos = 0
    consume = lambda n, writes='': get_parameters(ns, pos, modes, n, writes)

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
            ns[a] = inp

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

        elif op == 99:
            return

        else:
            raise RuntimeError(op)
