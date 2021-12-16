import functools as ft
import operator as op


opes = {
    0: sum,
    1: lambda ns: ft.reduce(op.mul, ns),
    2: min,
    3: max,
    4: None,
    5: lambda ns: op.gt(ns[0], ns[1]),
    6: lambda ns: op.lt(ns[0], ns[1]),
    7: lambda ns: op.eq(ns[0], ns[1]),
}


def read(stream, n):
    return int(''.join(next(stream) for _ in range(n)), 2)


def literal(stream):
    coll = 0
    while next(stream) == '1':
        coll |= read(stream, 4)
        coll <<= 4
    coll |= read(stream, 4)
    return coll


def consume(stream):
    ver = read(stream, 3)
    vers.append(ver)
    tid = read(stream, 3)
    ope = opes[tid]
    if ope is None:
        return literal(stream)
    else:
        I = next(stream)
        if I == '1':
            length = read(stream, 11)
            ns = [consume(stream) for _ in range(length)]
            return ope(ns)
        elif I == '0':
            length = read(stream, 15)
            sub = (next(stream) for _ in range(length))
            ns = []
            while True:
                try:
                    ns.append(consume(sub))
                except RuntimeError:
                    break
            return ope(ns)


vers = []
text = open(0).read().strip()
stream = iter(''.join(f'{int(char, 16):0>4b}' for char in text))
ans = consume(stream)
print(sum(vers))
print(ans)
