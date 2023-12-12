import functools
import re


@functools.lru_cache(maxsize=None)
def get_combos(pattern, ns):
    out = 0
    if not ns:
        new = '_' * len(pattern)
        if re.fullmatch(pattern, new):
            out += 1
    else:
        n, *ns = ns
        i_max = len(pattern) - sum(ns) - len(ns) - n + 1
        for i in range(i_max):
            new = '_' * i + '#' * n + '_' * (len(pattern) > i + n)
            if re.fullmatch(pattern[:len(new)], new):
                out += get_combos(pattern[len(new):], tuple(ns))
    return out


def combos(line, N=1):
    pattern, ns = line.split()
    # expand
    pattern = '?'.join([pattern] * N)
    ns = ','.join([ns] * N)
    # parse
    pattern = pattern.replace('.', '_').replace('?', '.')
    ns = [int(n) for n in ns.split(',')]
    return get_combos(pattern, tuple(ns))


text = open(0).read()
print(sum(combos(line) for line in text.splitlines()))
print(sum(combos(line, 5) for line in text.splitlines()))
