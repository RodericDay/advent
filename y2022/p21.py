from functools import lru_cache


@lru_cache(maxsize=None)
def fn(seed=None):
    instructions = map(str.split, text.replace(':', '').splitlines())
    while instructions:
        act, *instructions = instructions
        try:
            match act:
                case ['root', a, _, b] if seed is not None:
                    return eval(a) - eval(b)
                case ['humn', _] if seed is not None:
                    locals()['humn'] = seed
                case [name, a, x, b]:
                    locals()[name] = eval(a + x + b)
                case [name, a]:
                    locals()[name] = eval(a)
                case default:
                    raise RuntimeError(default)
        except NameError:
            instructions.append(act)
    return int(locals()['root'])


def bisect(fn, x1, x2):
    for _ in range(100):
        xn = x1 + (x2 - x1) // 2
        if fn(xn) == 0:
            return xn
        elif abs(fn(x1)) > abs(fn(x2)):
            x1 = xn
        else:
            x2 = xn


text = open(0).read()
print(fn())
print(bisect(fn, 0, 10_000_000_000_000))
