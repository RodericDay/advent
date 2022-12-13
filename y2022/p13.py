from functools import cmp_to_key


def cmp(aa, bb):
    match aa, bb:
        case int(), int():
            return (aa > bb) - (aa < bb)
        case int(), list():
            return cmp([aa], bb)
        case list(), int():
            return cmp(aa, [bb])
        case list(), list():
            fallback = cmp(len(aa), len(bb))
            return next((res for res in map(cmp, aa, bb) if res), fallback)


text = open(0).read()
pairs = [[eval(ln) for ln in block.splitlines()] for block in text.strip().split('\n\n')]
print(sum(i for i, (aa, bb) in enumerate(pairs, 1) if cmp(aa, bb) == -1))

x, y = [2], [6]
entries = sum(pairs, [x, y])
entries.sort(key=cmp_to_key(cmp))
print(entries.index(x) * entries.index(y))
