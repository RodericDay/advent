import sys


def get(x):
    return regs[x] if x in regs else int(x)


def cpy(x, y):
    regs[y] = get(x)


def inc(x):
    regs[x] += 1


def dec(x):
    regs[x] -= 1


def jnz(x, y):
    if get(x) != 0:
        return int(y)


def run(regs, lim=1000):
    pos = 0
    seen = {}
    for _ in range(lim):
        fn, *args = instructions[pos].split()
        pos += eval(fn)(*args) or 1
        if regs['d'] not in seen:
            seen[regs['d']] = regs['a']
    print(sorted(seen))


text = sys.stdin.read()
instructions = text.splitlines()

regs = {k: 0 for k in 'abcd'}
run(regs)
regs['c'] = 1
run(regs)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b


print(fib(27) + 19 * 11)
print(fib(34) + 19 * 11)
