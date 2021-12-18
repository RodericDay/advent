from functools import reduce
from itertools import permutations


text = open(0).read()
inp = [eval(line) for line in text.splitlines()]


def explode(state):
    last = None
    carry = None
    def mut(parent, idx, depth=1):
        nonlocal last, carry
        if type(parent[idx]) == int:
            last = parent, idx
            if carry:
                parent[idx] += carry
                raise RuntimeError
        elif carry is None and depth == 4:
            x, y = parent[idx]
            if last:
                p, j = last
                p[j] += x
            carry = y
            parent[idx] = 0
        else:
            mut(parent[idx], 0, depth + 1)
            mut(parent[idx], 1, depth + 1)
    try:
        mut(state, 0)
        mut(state, 1)
    except RuntimeError:
        pass
    return carry is not None


def split(state):
    def mut(par, idx):
        if type(par[idx]) == int:
            N = int(par[idx])
            if N >= 10:
                par[idx] = [N // 2, N // 2 + (N & 1)]
                raise RuntimeError
        else:
            mut(par[idx], 0)
            mut(par[idx], 1)
    try:
        mut(state, 0)
        mut(state, 1)
    except RuntimeError:
        return True


def add(a, b):
    state = eval(str([a, b]))
    while True:
        if explode(state):
            continue
        elif split(state):
            continue
        else:
            break
    return state


def magnitude(seq):
    if type(seq) == int:
        return seq
    x, y = seq
    return 3 * magnitude(x) + 2 * magnitude(y)


print(magnitude(reduce(add, inp)))
print(max(magnitude(add(*pair)) for pair in permutations(inp, 2)))
