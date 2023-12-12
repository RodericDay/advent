def solve(string, count):
    plain = [ln for ln in string.splitlines()]
    transposed = [''.join(ln) for ln in zip(*string.splitlines())]
    for grid, m in [(plain, 100), (transposed, 1)]:
        for idx in range(1, len(grid)):
            aa, bb = '\n'.join(grid[:idx][::-1]), '\n'.join(grid[idx:])
            aa, bb = sorted([aa, bb], key=len)
            aa, bb = set(enumerate(aa)), set(enumerate(bb))
            if len(aa - bb) == count:
                return idx * m


strings = open(0).read().split('\n\n')
print(sum(solve(string, 0) for string in strings))
print(sum(solve(string, 1) for string in strings))
