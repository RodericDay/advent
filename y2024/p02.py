def variants(row):
    for i in range(len(row)):
        yield row[:i] + row[i + 1:]


def differ(row):
    for a, b in zip(row, row[1:]):
        yield b - a


def is_safe(row, dampen=0):
    diffs = list(differ(row))
    if all(d < 0 for d in diffs) or all(d > 0 for d in diffs):
        if all(1 <= abs(d) <= 3 for d in diffs):
            return True
    if not dampen:
        return False
    else:
        return any(is_safe(sub) for sub in variants(row))


inp = open(0).read()
grid = [[int(n) for n in row.split()] for row in inp.splitlines()]
print(sum(is_safe(row) for row in grid))
print(sum(is_safe(row, dampen=1) for row in grid))
