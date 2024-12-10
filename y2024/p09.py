import itertools

inp = open(0).read().strip()
NULL = -1

stack = []
for idx, n in enumerate(map(int, inp)):
    if idx % 2:
        stack += [NULL] * n
    else:
        stack += [idx // 2] * n

def sort1(stack):
    stack = list(stack)
    for idx, cell in enumerate(stack):
        if cell == NULL:
            while stack[-1] == NULL:
                stack.pop()
            stack[idx] = stack.pop()
    return stack

def sort2(stack):
    pairs = [(k, len(list(vs))) for k, vs in itertools.groupby(stack)]
    N = max(n for n, _ in pairs)
    for x in range(N, 0, -1):
        # splice
        idx = next(i for i, (n, c) in enumerate(pairs) if n == x)
        n, c = pairs[idx]
        pairs[idx:idx + 1] = [(-1, c)]

        # insert
        for idx, (m, d) in enumerate(pairs):
            if m == NULL and d >= c:
                pairs[idx: idx + 1] = [(n, c), (m, d - c)]
                break
        else:
            pairs.append((n, c))

    return [n if n != NULL else 0 for n, c in pairs for _ in range(c)]

print(sum(i * v for i, v in enumerate(sort1(stack))))
print(sum(i * v for i, v in enumerate(sort2(stack))))
